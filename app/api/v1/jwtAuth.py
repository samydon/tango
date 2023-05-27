from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, status, Form
from sqlalchemy import func
from typing import Optional
from com import models, schemas
from com.database import get_db
import hashlib
from datetime import datetime, timedelta
import base64
import jwt
from com.config import settings


router = APIRouter()


def get_user(userId:str,db: Session = Depends(get_db)) -> models.User:
    db_user = db.query(models.User).filter(models.User.userId == userId).first()
    if not db_user:
        raise HTTPException(401, "Not registred")
    return db_user

@router.get("/token")
def get_jwt_token(userId:str,db: Session = Depends(get_db)):
    db_user =  get_user(userId,db)
    
    expire = datetime.utcnow() + (timedelta(minutes=30))
    header = {"alg":"HS256","type":"JWT"}
    payload   = {
        "id": db_user.userId,
        "auth": str(db_user.grade),
        "exp": expire,
    }
        
   # bytHeader = str(header).encode('utf-8')
   # header = base64.b64encode(bytHeader)
         
     
    #bytData = str(data).encode('utf-8')
    #data = base64.b64encode(bytData)    
    
    
    jwt_token = jwt.encode(payload, key=settings.JWT_KEY.get_secret_value(), algorithm="HS256")
        
    
    #jwt_tocken = f'{str(header)}.{str(data)}.{enc_data}'       
    
    
    
    
    return {"token":f"{jwt_token}"}

  
      
   # return db.query(models.User).all()

