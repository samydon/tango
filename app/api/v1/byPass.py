from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, status, Form
from sqlalchemy import func

from com import models, schemas
from com.database import get_db
import hashlib
from datetime import datetime


router = APIRouter()


async def add_user(userId: str,userName: str, nickName:str, email:str, phone:str, db: Session) -> models.User:
 
    ct = str(datetime.datetime.now().timestamp() * 1000)
    orgStr = f'{ct}{userId}'
    hash_value = hashlib.sha256(orgStr.encode("utf-8")).hexdigest()
   

    row = models.User(sysId= hash_value, userId=userId,userName=userName,nickName = nickName,email=email,phone=phone)
    db.add(row)
    db.commit()
    return row

#반환형식이 리스트일 경우 1개여도 오류발생이 인되게
@router.get("/list", response_model= List[schemas.User])
async def get_user_list(userid:str=None,username:str=None,db: Session = Depends(get_db)):


    return list(db.query(models.User).filter_by(userId=userid))
      
   # return db.query(models.User).all()

