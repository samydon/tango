from typing import List,Optional

from fastapi import APIRouter, Depends,Header
from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, status, Form
from sqlalchemy import func

from com import models, schemas
from com.database import get_db
import hashlib
from datetime import datetime
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from sqlalchemy import and_, or_

#OAuth Form
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/jwt/token")

router = APIRouter()


async def add_user(userId: str,userName: str, nickName:str, email:str, phone:str, grade:int, db: Session) -> models.User:
 
    #시스템 아이디
    ct = str(datetime.now().timestamp() * 1000)
    orgStr = f'{ct}{userId}'
    hash_value = hashlib.sha256(orgStr.encode("utf-8")).hexdigest()
   

    row = models.User(sysId= hash_value, userId=userId,userName=userName,nickName = nickName,email=email,phone=phone,grade=grade)
    db.add(row)
    db.commit()
    return row



@router.get("/list2", response_model= List[schemas.user])
async def get_user_list(token: Annotated[str, Depends(oauth2_scheme)],userid:str="",username:str="",db: Session = Depends(get_db)):
        print(f'nuser id:{userid}')
        if userid == None and username == None:
            return list(db.query(models.User).all())
        else:
            return list(db.query(models.User).filter(models.User.userId.like(f'%{userid}%'),models.User.userName.like(f'%{username}%')).all())
        

#반환형식이 리스트일 경우 1개여도 오류발생이 인되게
@router.get("/list", response_model= List[schemas.user])
async def get_user_list(userid:str="",username:str="",db: Session = Depends(get_db)):

    if userid == None and username == None:
        return list(db.query(models.User).all())
    else:
        return list(db.query(models.User).filter(models.User.userId.like(f'%{userid}%'),models.User.userName.like(f'%{username}%')).all())
            
      
   # return db.query(models.User).all()


@router.post("", response_model=schemas.ResponseUsr, status_code=status.HTTP_201_CREATED)
async def add_user_json(data: schemas.UserCreate, db: Session = Depends(get_db)):
    return await add_user(**data.dict(), db=db)


@router.post("/form", response_model=schemas.ResponseUsr, status_code=status.HTTP_201_CREATED)
async def add_user_redirect(    
    userId: str = Form(..., title="사용자아이디"),
    userName: str = Form(..., title="사용자이름"),
    nickName: str = Form(..., title="별명"),
    email:str = Form(default=None, title="이메일"),
    phone:str = Form(default=None, title="핸드폰번호"),
    grade:int = Form(default=None, title="등급"),
    db: Session = Depends(get_db),
):
    return await add_user(userId,userName,nickName,email,phone,grade,db)
