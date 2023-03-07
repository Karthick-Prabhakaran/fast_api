from fastapi import APIRouter

user = APIRouter(prefix='/add',
                 tags=['addition'])

@user.get('/numbers')
def adding_numbers():
    return {"message":"add two numbers"}