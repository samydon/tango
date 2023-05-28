from pydantic import BaseModel, Field
from typing import Optional



class ResourceId(BaseModel):
    id: int

    class Config:
        orm_mode = True


class user(BaseModel):
    sysId: str
    userId: str
    userName: str
    nickName: str
    email: Optional[str]
    phone: Optional[str]
    grade: Optional[int]
    class Config:
        orm_mode = True

class ResponseUsr(BaseModel):
    userId: str
    userName: str
    
    class Config:
        orm_mode = True

class UserCreate(BaseModel):    
    userId:str = Field(..., title="사용자아이디", example="naver123")
    userName:str = Field(..., title="사용자이름", example="홍길동")
    nickName:str = Field(..., title="별병", example="미친사자")
    email:str = Field(...,title="이메일",example="sample@example.com")
    phone:str = Field(...,title="핸드폰",example="010-0000-0000")
    grade:int = Field(...,title="등급")
    
class Token(BaseModel):
    access_token: str
    token_type: str
