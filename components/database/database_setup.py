# Database related setup to store travel plan
from pathlib import Path
from config import setting

from sqlalchemy import create_engine, Integer, String, Text, DateTime, Column
from sqlalchemy.orm import declarative_base, sessionmaker

Path("db").mkdir(exist_ok=True)

database_url = setting.DATABASE_URL
print("inside database_setup.py file and data folder and db url created\n")
engine = create_engine(
    database_url,
    connect_args = {"check_same_thread": False}
)
print("connection engine for db created")
SessionLocal = sessionmaker(
    bind=engine, 
    autoflush=False, 
    autocommit= False
)
print("local session for db created\n")
Base = declarative_base()




def init_db():
    Base.metadata.create_all(bind=engine)
    print("init_db method inside")






