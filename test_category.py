import unittest

from Category import Category
from Database import Database
from TypeFlow import TypeFlow
from answer import text_answer


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.session = Database.get_instance().session()

    def test_add_category_transport(self):
        answer = text_answer('Wallet добавь категорию расходов транспорт')
        self.assertEqual('Категория транспорт добавлена!', answer)

    def test_add_category_work(self):
        answer = text_answer('Wallet добавь категорию доходов работа')
        self.assertEqual('Категория работа добавлена!', answer)

    def test_add_category_transport_in_base(self):
        text_answer('Wallet добавь категорию расходов транспорт')
        category = self.session.query(Category).first()
        self.assertIsNotNone(category)
        self.assertEqual('транспорт', category.name)
        self.assertEqual(TypeFlow.PROFIT, category.type)
