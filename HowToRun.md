python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt

python src/train_diabetes_model.py
python manage.py migrate
python manage.py runserver 8000
