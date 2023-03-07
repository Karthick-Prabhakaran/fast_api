from sqlalchemy import create_engine,MetaData
from sqlalchemy import create_engine, Column,TEXT,BIGINT,DOUBLE
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel


meta =  MetaData()
db_user = 'user'
db_pwd = 'root'
db_host = 'host.docker.internal'
db_port = '3307'
db_name = 'db'
# # connection string
connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_str)
Base = declarative_base()


# Define To Do class inheriting from Base
class ToDo(Base):
    __tablename__ = 'users'
    s_no = Column(BIGINT, primary_key=True)
    deal_Date = Column(TEXT(256))
    security_code=Column(BIGINT)
    security_name=Column(TEXT(250))
    client_name=Column(TEXT(250))
    deal_type=Column(TEXT(250))
    quantity=Column(BIGINT)
    price=Column(DOUBLE)

# Create ToDoRequest Base Model
class ToDoRequest(BaseModel):
    s_no: int
    deal_Date: str
    security_code: int
    security_name: str
    client_name: str
    deal_type: str
    quantity: int
    price: float   


# Create the database
Base.metadata.create_all(engine)
connection = engine.connect()
print(connection)