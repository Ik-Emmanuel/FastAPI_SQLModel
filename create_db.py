from sqlmodel import  SQLModel
from database import engine
from models import Item

print("CREATING DATABASE .....")

SQLModel.metadata.create_all(engine)