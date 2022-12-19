python -m venv ./venv
.\venv\Scripts\activate

pip install -r requirements.txt

python create_db.py

alembic revision --autogenerate -m "Init"  
alembic upgrade head