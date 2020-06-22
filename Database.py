from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from base import Base


class Database:
    __instance = None

    def __init__(self):
        with open('database_name.txt') as f:
            database_name = f.readline()
            self.engine = create_engine(database_name, echo=True)
            Base.metadata.create_all(self.engine)

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Database()
        return cls.__instance

    def session(self) -> Session:
        return sessionmaker(bind=self.engine)()
