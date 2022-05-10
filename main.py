from typing import Optional , List
from unittest import result
from fastapi import FastAPI, status, HTTPException
from models import Item
from database import engine
from sqlmodel import Session, select

app = FastAPI()

session=Session(bind=engine)

"""
The way SQLModel works is 
- generate a statement
- excute the statement using the binded engine 
"""

@app.get("/items", response_model=List[Item], status_code= status.HTTP_200_OK)
async def get_all_items():
    statement = select(Item)
    result =  session.exec(statement).all()
    return result


@app.get("/items/{item_id}", response_model=Item)
async def get_one_items(item_id:int):
    statement = select(Item).where(Item.id == item_id)
    result = session.exec(statement).first()  #or .one_or_none() or .one()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return result
    

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_an_items(item:Item):
    new_item = Item(title=item.title, description=item.description)
    session.add(new_item)
    session.commit()
    return new_item
 


@app.put("/items/{item_id}", response_model=Item, status_code=status.HTTP_202_ACCEPTED)
async def update_one_item(item_id:int, item:Item):
    statement = select(Item).where(Item.id == item_id)
    result = session.exec(statement).first()
    result.title = item.title
    result.description = item.description
    session.commit()
    return result



@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id:int):
    statement= select(Item).where(Item.id == item_id)
    result = session.exec(statement).one_or_none()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The specified resource was not found")
    session.delete(result)
    return result
