from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

db = create_engine('sqlite:///tutorial.db', echo=True)

metadata = MetaData()

users_talbe = Table('users', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('fullname', String),
    Column('password', String),
)

metadata.create_all(db)


