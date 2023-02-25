from sqlalchemy import Table, Column, String
from src.db import metadata_obj

queue_table = Table(
    'queue',
    metadata_obj,
    Column('id', String, primary_key=True),
    Column('name', String()),
    mysql_engine='InnoDB'
)
