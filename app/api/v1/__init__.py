from fastapi import APIRouter, Depends


from . import user,jwtAuth


router = APIRouter()
#router.include_router(webhook.router, prefix="/webhook", dependencies=[Depends(get_user)])
#router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(user.router, prefix="/users", tags=["User"])
router.include_router(jwtAuth.router, prefix="/users", tags=["Jwt"])
#router.include_router(reservoir.router, prefix="/reservoir", tags=["Reservoir"])