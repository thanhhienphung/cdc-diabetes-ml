import os
import pickle

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

FEATURES = [
    'HighBP',
    'HighChol',
    'CholCheck',
    'BMI',
    'Smoker',
    'Stroke',
    'HeartDiseaseorAttack',
    'PhysActivity',
    'Fruits',
    'Veggies',
    'HvyAlcoholConsump',
    'AnyHealthcare',
    'NoDocbcCost',
    'GenHlth',
    'MentHlth',
    'PhysHlth',
    'DiffWalk',
    'Sex',
    'Age',
    'Education',
    'Income',
]

TARGET = 'Diabetes_012'

LABEL_MAP = {
    0: 'non-diabetic',
    1: 'pre-diabetic',
    2: 'diabetic',
}


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'diabetes_012_health_indicators_BRFSS2015.csv')

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at {data_path}")

    df = pd.read_csv(data_path)

    needed_cols = [TARGET] + FEATURES
    missing_cols = [col for col in needed_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in dataset: {', '.join(missing_cols)}")

    df = df[needed_cols].dropna()

    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    # Older scikit-learn versions do not accept multi_class; fall back safely.
    try:
        classifier = LogisticRegression(
            max_iter=500,
            multi_class='multinomial',
            class_weight='balanced',
        )
    except TypeError:
        classifier = LogisticRegression(
            max_iter=500,
            class_weight='balanced',
        )

    model = Pipeline(
        steps=[
            ('scaler', StandardScaler()),
            ('classifier', classifier),
        ]
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print('Accuracy:', accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))

    model_dir = os.path.join(base_dir, 'resources', 'models')
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, 'diabetes_model_v1.pkl')

    bundle = {
        'model': model,
        'features': FEATURES,
        'label_map': LABEL_MAP,
    }

    with open(model_path, 'wb') as file_handle:
        pickle.dump(bundle, file_handle)

    print(f"Model saved to {model_path}")


if __name__ == '__main__':
    main()
