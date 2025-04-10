from typing import Optional,List
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    __tablename__ = "user"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    code: str
    tasks: list["Task"] = Relationship(back_populates="user")



