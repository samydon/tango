from typing import List,Optional

from fastapi import APIRouter, Depends,Header
from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, status, Form
from schemas.moneygram import responseModel, requestModel
from typing import Annotated
from pydantic import Required

router = APIRouter()

@router.get("/transaction", response_model= List[responseModel.Senderinfo])
async def get_transaction_list(agentId: str = Header(Required), agentSeq:str = Header(Required),token:str = Header(Required),language:str|None = Header(default="en"),timeStamp:str = Header(None),cientSoftwareVersion:str = Header(None),channelType:str|None = Header(default="ATM")):
    return {"test":"OK"}



@router.get("/feeLookup", response_model= List[responseModel.Senderinfo])
async def get_fee_lookup(agentId: str = Header(Required), agentSeq:str = Header(Required),token:str = Header(Required),language:str|None = Header(default="en"),timeStamp:str = Header(None),cientSoftwareVersion:str = Header(None),channelType:str|None = Header(default="ATM")):
    return {"test":"OK"}

