from sqlmodel import Session, select
from ..models.user import User
from .password_manager import PasswordManager


class UserRepository():

    def __init__(self, session: Session):
        self.session = session
        self.pw_manager = PasswordManager()
        

    def _create_user(self, dados: dict) -> User:

        copia_dados = dados.copy()

        old_password = copia_dados.pop('password')
        password_hash = self.pw_manager.hash_password(old_password)
        user = User(**dados, password=password_hash)

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user
    

    def _get_by_id(self, user_id: int) -> User | None:

        return self.session.get(User, user_id)

    def _get_all(self) -> list[User]:

        statement = select(User)
        return self.session.exec(statement).all()
    
    def _put(self, user_id, dados: dict) -> User:

        user = self.session.get(User, user_id)

        for key, value in dados.items():
            setattr(user, key, value)

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    

