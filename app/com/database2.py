import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sshtunnel import SSHTunnelForwarder
#from config   import settings


#engine = create_engine(
#    "mysql+pymysql://{username}:{password}@{host}:{port}/{name}?charset=utf8mb4".format(
#        username=settings.DB_USERNAME,
 #       password=settings.DB_PASSWORD.get_secret_value(),
  #      host=settings.DB_HOST,
#        port=settings.DB_PORT,
#        name=settings.DB_NAME,
#    ),
#    connect_args={"ssl": {"ca": "/app/ca.pem"}} if os.getenv("APP_ENV") == "prod" else {},
#)




ssh_tunnel = SSHTunnelForwarder (
    ('',22),
    ssh_username="ec2-user",
    ssh_pkey="",
    remote_bind_address=('',3306)
) 

ssh_tunnel.start()

#engine = create_engine('mysql+pymysql://admin:admin12#$@oooall-db.c2w4be7rtxdi.ap-northeast-2.rds.amazonaws.com:'+str(ssh_tunnel.local_bind_port)+'/apitest')


    
engine = create_engine('mysql+mysqldb://:a@oßs.amazonaws.com:%s/apitest' % ssh_tunnel.local_bind_port)




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
        
