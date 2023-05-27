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
    ('bastion.oooall.com',22),
    ssh_username="ec2-user",
    ssh_pkey="/Users/samjinkim/Documents/oooall_bastion.pem",
    remote_bind_address=('oooall-db.c2w4be7rtxdi.ap-northeast-2.rds.amazonaws.com',3306)
) 

print('터널링 준비')
ssh_tunnel.start()

print('터널링 시작')

#engine = create_engine('mysql+pymysql://admin:admin12#$@oooall-db.c2w4be7rtxdi.ap-northeast-2.rds.amazonaws.com:'+str(ssh_tunnel.local_bind_port)+'/apitest')


    
engine = create_engine('mysql+mysqldb://admin:admin12#$@oooall-db.c2w4be7rtxdi.ap-northeast-2.rds.amazonaws.com:%s/apitest' % ssh_tunnel.local_bind_port)



print('db 연결 완료')

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
        
