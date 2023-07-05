
from pydantic import BaseModel, Field
from typing import Optional,List

class ReceiverInfo(BaseModel):    
    receiveCountry: str =  Field(..., title="사용자아이디", example="usa")
    receiverFirstName: str = Field(..., title="사용자아이디", example="samy")
    receiverMiddleName: Optional[str] = Field(default="", title="", example="")
    receiverLastName: str = Field(..., title="수신자마지막이름", example="kim")
    receiverLastName2: Optional[str] =  Field(default="", title="", example="")
    receiverAddress: str = Field(..., title="", example="")
    receiverAddress2: str = Field(..., title="", example="")
    receiverAddress3: str = Field(..., title="", example="")
    receiverAddress4: str = Field(..., title="", example="")
    receiverCity: str = Field(..., title="", example="")
    receiverState: str = Field(..., title="", example="")
    receiverZipCode: str = Field(..., title="", example="")
    receiverCountry: str = Field(..., title="", example="")
    receiverPhone: str = Field(..., title="", example="")
    sendAmount: str = Field(..., title="", example="")
    deliveryOption: str = Field(..., title="", example="")
    sendCurrency: str = Field(..., title="", example="USA")
    direction1: str = Field(..., title="", example="")
    direction2: str = Field(..., title="", example="")
    direction3: str = Field(..., title="", example="")
    customerReceiveNumber: str = Field(..., title="", example="")
    accountNickname: str = Field(..., title="", example="")
    displayAccountID: str = Field(..., title="", example="")
    receiveAgentID: str = Field(..., title="", example="")
    receiveAgentName: str = Field(..., title="", example="")
    receiveAgentAbbreviation: str = Field(..., title="", example="")
    receiveCurrency: str = Field(..., title="", example="")
    payoutCurrency: str = Field(..., title="", example="")
    receiverPhoneCountryCode: str = Field(..., title="", example="")
   
   
class Senderinfo(BaseModel):
    senderFirstName: str = Field(..., title="", example="")
    senderMiddleName:  Optional[str] = Field(default="", title="", example="")
    senderLastName: str = Field(..., title="", example="")
    senderLastName2:  Optional[str] = Field(default="", title="", example="")
    senderAddress:  Optional[str] = Field(default="", title="", example="")
    senderAddress2:  Optional[str] = Field(default="", title="", example="")
    senderAddress3:  Optional[str] = Field(..., title="", example="")
    senderAddress4:  Optional[str] = Field(..., title="", example="naver123")
    senderCity: str = Field(..., title="", example="naver123") 
    senderState: str = Field(..., title="", example="naver123") 
    senderZipCode: str = Field(..., title="", example="naver123")
    senderCountry: str = Field(..., title="", example="naver123")
    senderHomePhone: str = Field(..., title="사용자아이디", example="naver123")
    freqCustCardNumber: str = Field(..., title="사용자아이디", example="naver123")
    agentFrequentCustomerNumber: str = Field(..., title="사용자아이디", example="naver123")
    consumerId: str = Field(..., title="사용자아이디", example="naver123") 
    senderBirthCountry: str = Field(..., title="사용자아이디", example="naver123")
    senderDOB: str = Field(..., title="사용자아이디", example="naver123") 
    senderHomePhoneCountryCode: str = Field(..., title="사용자아이디", example="naver123")
    senderTransactionEmailNotificationOptIn: str = Field(..., title="사용자아이디", example="naver123")
    senderTransactionSMSNotificationOptIn: str = Field(..., title="사용자아이디", example="naver123")
    senderMarketingEmailNotificationOptIn: str = Field(..., title="사용자아이디", example="naver123")
    senderMarketingSMSNotificationOptIn: str = Field(..., title="사용자아이디", example="naver123")
    senderEmailAddress: str = Field(..., title="사용자아이디", example="naver123")
    senderMobilePhone: str = Field(..., title="사용자아이디", example="naver123")
    receiverInfo: List[ReceiverInfo] 
    
    class Config:
        orm_mode = True


