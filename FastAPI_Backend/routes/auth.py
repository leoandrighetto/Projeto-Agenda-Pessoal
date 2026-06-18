from fastapi import APIRouter
from repositories.user_repository import UserRepository
from models.user import User

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post("/register")
async def register(self, data: dict) -> User:

    print(data)

    return {"teste": "Passou"}

    """
    
    1 - Recebe os dados vindos do frontend  <--

    2 - Sanitiza os dados 
    3 - Valida se os dados estão completos e dentro das regras de negócio
    4 - Se os dados estiverem completos, insere o usuário no banco de dados
    5 - Cria uma sessão de usuário com um hash JWT
    
    """
