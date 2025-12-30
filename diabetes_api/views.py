import json
import os
import pickle

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

MODEL_REL_PATH = os.path.join(
    settings.BASE_DIR,
    'resources',
    'models',
    'diabetes_model_v1.pkl',
)

_model_bundle = None


def load_model():
    global _model_bundle
    if _model_bundle is None:
        if not os.path.exists(MODEL_REL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_REL_PATH}")
        with open(MODEL_REL_PATH, 'rb') as file_handle:
            _model_bundle = pickle.load(file_handle)
    return _model_bundle


def _extract_features(payload, feature_names):
    if isinstance(payload, dict):
        missing = [name for name in feature_names if name not in payload]
        if missing:
            raise ValueError(f"Missing features: {', '.join(missing)}")
        values = [payload[name] for name in feature_names]
    elif isinstance(payload, list):
        if len(payload) != len(feature_names):
            raise ValueError(
                f"Expected {len(feature_names)} feature values, got {len(payload)}"
            )
        values = payload
    else:
        raise ValueError("Features must be a dict or list")

    try:
        return [float(value) for value in values]
    except Exception as exc:
        raise ValueError("All feature values must be numeric") from exc


@csrf_exempt
def predict_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST is allowed'}, status=405)

    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        return JsonResponse({'error': 'Invalid JSON body'}, status=400)

    if not isinstance(data, dict):
        return JsonResponse({'error': 'Request JSON must be an object'}, status=400)

    try:
        bundle = load_model()
        model = bundle['model']
        feature_names = bundle.get('features', [])
        label_map = bundle.get('label_map', {})

        payload = data.get('features', data)
        features = _extract_features(payload, feature_names)

        prediction = model.predict([features])[0]
        pred_class = int(prediction)
        label = label_map.get(pred_class, str(pred_class))

        probabilities = None
        if hasattr(model, 'predict_proba'):
            proba = model.predict_proba([features])[0]
            classes = list(getattr(model, 'classes_', range(len(proba))))
            probabilities = {str(c): float(p) for c, p in zip(classes, proba)}

        return JsonResponse(
            {
                'prediction': pred_class,
                'label': label,
                'probabilities': probabilities,
            }
        )
    except FileNotFoundError as exc:
        return JsonResponse({'error': str(exc)}, status=500)
    except ValueError as exc:
        return JsonResponse({'error': str(exc)}, status=400)
    except Exception as exc:
        return JsonResponse(
            {'error': f'Prediction failed: {exc.__class__.__name__}: {exc}'},
            status=500,
        )
