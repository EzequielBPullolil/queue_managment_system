
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

USERNAME = os.environ['DB_USERNAME']
PASSWORD = os.environ['DB_PASSWORD']
HOST = os.environ['DB_HOST']
DBNAME = os.environ['DB_NAME']

connection_url = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DBNAME}?charset=utf8mb4'


# App use variables
engine = create_engine(connection_url, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
