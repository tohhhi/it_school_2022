from fastapi import Body
from pydantic import BaseModel



class Todo(BaseModel):
    title: str # type annotation
    body: str

