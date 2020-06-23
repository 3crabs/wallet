from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Flow(Base):
    __tablename__ = 'flows'
    id = Column(Integer, primary_key=True)
    money = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", backref='flows')

    def __init__(self, money, category_id: int):
        self.money = money
        self.category_id = category_id
