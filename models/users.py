from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta

user_model= Table(
    'users',meta,
    Column('id', Integer,primary_key=True, autoincrement=True ),
    Column('email', String(400), index=True, unique=True, nullable=False),
    Column('username', String(400), nullable=False),
    Column('password', String(1000), nullable=False)
)

meta.create_all(engine)