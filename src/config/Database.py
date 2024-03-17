from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

class Database:
    def __init__(self):
        self.engine = self.create_engine()
        self.SessionLocal = self.create_session()

    def create_engine(self):
        database_url = self.get_database_url()
        print("[I18] - Creating connection")
        return create_engine(database_url)

    def get_database_url(self):
        return f'mysql+pymysql://{os.getenv("user")}:{os.getenv("pass")}@{os.getenv("host")}:{os.getenv("port")}/{os.getenv("database")}'

    def create_session(self):
        print("[I24] - Creating session")
        return sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        print("[I27] - Get session")
        return self.SessionLocal()

    def create_tables(self):
        print("[I30] - Creating tables...")
        Base.metadata.create_all(bind=self.engine)
