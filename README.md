# FastAPI_SQLModel
working with SQLModel with FastAPI which combines pydantic and SQLAlchemy into one 


## Advantages
- SQLModel allows for ease of data validation as well as db model creation 
- No need for separate validation models and database models using one schema



## Steps 
- create your models (models.py)
    -- from sqlmodel import SQLModel, Field
        class Item(SQLModel, table=True):
            id: Optional[int] = Field(default=None, primary_key=True)
            title:str
            description:str


- create database engine (database.py)
    from sqlmodel import  create_engine

    conn_str=f"{Your DATABASE Connection string}"
    engine = create_engine(conn_str, echo=True)


-  Next create your tables in the db 
    from sqlmodel import  SQLModel
    from database import engine
    from models import (ALL Models created)

    SQLModel.metadata.create_all(engine) //This creates the tables 
    // make sure the 3 imports are complete