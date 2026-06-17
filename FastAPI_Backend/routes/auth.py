from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

class AuthRouter():

    @router.post("/register")
    async def register():
        pass