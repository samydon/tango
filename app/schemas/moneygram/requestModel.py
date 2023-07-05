
from pydantic import BaseModel, Field
from typing import Optional,List


class HeaderModel():
    agentID: str = Field(..., title="Location ID", example="TEST01")
    agentSequence: str = Field(..., title="agent 순번", example="02")
    token: str = Field(..., title="agent 비밀번호", example="")
    language: str = Field(default="en", title="언어", example="en")
    timeStamp: str = Field(defualt="", title="전송시간", example="")
    cientSoftwareVersion: str = Field(default="1.0", title="", example="1.3")
    channelType: str = Field(default="ATM", title="", example="POS")
    
    class Config:
        orm_mode = True

