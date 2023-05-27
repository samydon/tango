import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from sshtunnel import SSHTunnelForwarder
from .config   import settings

engine = create_engine(
    "mysql+pymysql://{username}:{password}@{host}:{port}/{name}?charset=utf8mb4".format(
        username=settings.DB_USERNAME,
        password=settings.DB_PASSWORD.get_secret_value(),
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        name=settings.DB_NAME,
   )
)
#engine = create_engine(f'mysql+pymysql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}')

#engine = create_engine('mysql+pymysql://root:admin12#$@0.0.0.0:3306/sampleapi')



SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
