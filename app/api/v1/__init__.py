from fastapi import APIRouter
#from . import user
from .sendtrans import sendMoneyGram


router = APIRouter()
#router.include_router(user.router, prefix="/users", tags=["User"])
router.include_router(sendMoneyGram.router, prefix="/sendtrans/mg", tags=["MoneyGram"])
