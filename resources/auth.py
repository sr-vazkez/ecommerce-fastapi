from fastapi import APIRouter
#Importando cosas creadas por uno
from managers.user import UserManager
from schemas.request.user import UserLoginIn, UserRegister


router = APIRouter(tags=["Auth"])

@router.post('/register/', status_code=201)
async def register(user_data: UserRegister):
    token =  await UserManager.register(user_data.dict())
    return{
        "token": token
    }

@router.post("/login/")
async def login(user_data: UserLoginIn):
    token = await UserManager.login(user_data.dict())
    return{"token":token}