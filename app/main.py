from fastapi import FastAPI, status,HTTPException
from app.config.db import connection,ToDoRequest,ToDo,engine
from sqlalchemy.orm import Session
import app.config.scrap_data_insert_db


app = FastAPI()


@app.get("/")
def root():
    return "Welcome to fast api demo. Try using /docs at the end to do CRUD operation"

@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(todo: ToDoRequest):

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)
    # create an instance of the database model
    tododb = ToDo(deal_Date= todo.deal_Date)
    # add it to the session and commit it
    session.add(tododb)
    session.commit()
    id = tododb.deal_Date
    # close the session
    session.close()
    # return the id
    return f"Added new item with deal_Date {id}"


@app.get("/todo/{s_no}")
def read_todo(s_no: int):

    session = Session(bind=engine, expire_on_commit=False)
    todo = session.query(ToDo).get(s_no)
    session.close()

    return f"todo item with s_no: {todo.s_no} and deal_date: {todo.deal_Date} {todo.security_code} {todo.security_name} {todo.client_name}"

@app.put("/todo/{s_no}")
def update_todo(s_no: int, client_name: str):

    session = Session(bind=engine, expire_on_commit=False)
    todo = session.query(ToDo).get(s_no)
    if todo:
        todo.client_name = client_name
        session.commit()
    session.close()
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {s_no} not found")

    return todo

@app.delete("/todo/{s_no}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(s_no: int):

    session = Session(bind=engine, expire_on_commit=False)
    todo = session.query(ToDo).get(s_no)
    if todo:
        session.delete(todo)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"todo item with id {s_no} not found")

    return None
