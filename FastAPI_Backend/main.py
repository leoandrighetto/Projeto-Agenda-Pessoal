from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine, get_session
from sqlmodel import SQLModel

# from models.model import model

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine) 
    yield
    print("Desligando a aplicação...")

app = FastAPI(lifespan=lifespan)