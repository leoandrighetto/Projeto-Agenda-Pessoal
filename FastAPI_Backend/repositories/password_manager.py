from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

class PasswordManager:
    def __init__(self):
        # O PasswordHasher já vem configurado de fábrica com os parâmetros 
        # recomendados pela RFC 9106 (padrão ouro para Argon2id)
        self.ph = PasswordHasher()

    def hash_password(self, password: str) -> str:
        """
        Gera o hash da senha em texto plano.
        O salt é gerado e embutido automaticamente na string de retorno.
        """
        return self.ph.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verifica se a senha em texto plano corresponde ao hash do banco.
        Retorna True se for válida, False se não for.
        """
        try:
            return self.ph.verify(hashed_password, plain_password)
        except VerifyMismatchError:
            return False