from typing import List

from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, status, Form
from sqlalchemy import func
from typing import Optional
from com import models, schemas
from com.database import get_db
import hashlib
from datetime import datetime, timedelta
import base64
from com.config import settings
import jwt
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()


def get_user(userId:str,userPasswd:str, db: Session = Depends(get_db)) -> models.User:
    db_user = db.query(models.User).filter(models.User.userId == userId).first()
    if not db_user:
        raise HTTPException(401, "Not registred")
    return db_user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    print(to_encode)
    additional_headers = {"alg":"HS256", "typ":"JWT",'kid': '0001'}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_KEY.get_secret_value(),headers=additional_headers, algorithm="HS256")
    return encoded_jwt

#@router.get("/token")
#def get_jwt_token(userId:str,db: Session = Depends(get_db)):
#    db_user =  get_user(userId,db)
    
#    expire = datetime.utcnow() + (timedelta(minutes=30))
#    header = {"alg":"HS256","type":"JWT"}
#    payload   = {
#        "id": db_user.userId,
#        "auth": str(db_user.grade),
#        "exp": expire,
#ß    }
        
   # bytHeader = str(header).encode('utf-8')
   # header = base64.b64encode(bytHeader)
         
     
    #bytData = str(data).encode('utf-8')
    #data = base64.b64encode(bytData)    
    
    
  #  jwt_token = jwt.encode(payload, key=settings.JWT_KEY.get_secret_value(), algorithm="HS256")
        
    
    #jwt_tocken = f'{str(header)}.{str(data)}.{enc_data}'       
    
    
    
    
  #  return {"token":f"{jwt_token}"}

 
@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],db:Session = Depends(get_db)) :
    user = get_user(form_data.username, form_data.password,db )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"uid": user.userId, "auth": str(user.grade)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
 
      
   # return db.query(models.User).all()

