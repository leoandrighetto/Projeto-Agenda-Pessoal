from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()
database = os.getenv('DATABASE_URL')
engine = create_engine(url=database)

def get_session():
    with Session(engine) as session:

        try:
            yield session
        finally:
            session.close()