# FastAPI_SQLModel
working with SQLModel with FastAPI which combines pydantic and SQLAlchemy into one 


## Advantages
- SQLModel allows for ease of data validation as well as db model creation 
- No need for separate validation models and database models using one schema



## Steps 
- create your models (models.py)
   using SQLModel and Fields: from sqlmodel import SQLModel, Field


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


## Crud Operations 

- Read ALL
    statement = select(Item)  
    result =  session.exec(statement).all()  

- Read One  
    statement = select(Item).where(Item.id == item_id)  
    result = session.exec(statement).first()  #or .one_or_none() or .one()  

- Create  
    new_item = Item(title=item.title, description=item.description)  
    session.add(new_item)  
    session.commit()  

- Update
    statement = select(Item).where(Item.id == item_id)  
    result = session.exec(statement).first()  
    result.title = item.title  
    result.description = item.description  
    session.commit()  


- Delete  
    statement= select(Item).where(Item.id == item_id)  
    result = session.exec(statement).one_or_none()  
    if not result:  
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The specified resource was not found")  
    session.delete(result)  

