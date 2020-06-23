from sqlalchemy import Column, Integer, String

from models.TypeFlow import TypeFlow
from models.Base import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)

    def __init__(self, name: str, type_flow: TypeFlow):
        self.name = name
        self.type = type_flow
