python3 -m venv ./venv
.\venv\Scripts\activate

pip3 install -r requirements.txt

python3 create_db.py

alembic revision --autogenerate -m "Init"  
alembic upgrade head