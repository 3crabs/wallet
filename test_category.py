import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Base
from Category import Category
from answer import text_answer


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()

    def test_add_category_transport(self):
        answer = text_answer('Wallet добавь категорию расходов транспорт')
        self.assertEqual('Категория транспорт добавлена!', answer)

    def test_add_category_work(self):
        answer = text_answer('Wallet добавь категорию доходов работа')
        self.assertEqual('Категория работа добавлена!', answer)

    def test_add_category_transport_in_base(self):
        text_answer('Wallet добавь категорию расходов транспорт')
        category = self.session.query(Category).first()
        self.assertEqual('транспорт', category.name)
        self.assertFalse(category.is_profit)


if __name__ == '__main__':
    unittest.main()
