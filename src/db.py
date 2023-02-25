from sqlalchemy import create_engine, MetaData
import os

USERNAME = os.environ['DB_USERNAME']
PASSWORD = os.environ['DB_PASSWORD']
HOST = os.environ['DB_HOST']
DBNAME = os.environ['DB_NAME']
connection_url = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DBNAME}?charset=utf8mb4'
engine = create_engine(connection_url, echo=True)


metadata_obj = MetaData()


metadata_obj.create_all(engine)
