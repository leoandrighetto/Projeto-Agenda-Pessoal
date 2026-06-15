from datetime import datetime
from sqlmodel import Field, SQLModel, Column
from sqlalchemy import Text, func


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(max_length=15, unique=True)
    fullname: str = Field(max_length=60)
    email: str = Field(max_length=100, unique=True)
    password: str = Field(sa_column=Column(Text, nullable=False))
    created_at: datetime = Field(sa_column_kwargs={"server_default": func.now()})
    updated_at: datetime = Field(
        sa_column_kwargs={"server_default": func.now(), "onupdate": func.now()}
    )
