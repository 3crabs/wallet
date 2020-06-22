import unittest

from Category import Category
from Database import Database
from TypeFlow import TypeFlow
from answer import text_answer


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.session = Database.new_base().session()

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
        self.assertEqual(TypeFlow.LESS, category.type)

    def test_add_category_work_in_base(self):
        text_answer('Wallet добавь категорию доходов работа')
        category = self.session.query(Category).first()
        self.assertIsNotNone(category)
        self.assertEqual('работа', category.name)
        self.assertEqual(TypeFlow.PROFIT, category.type)

    def test_add_bad_type_category(self):
        answer = text_answer('Wallet добавь категорию доходов работа')
        self.assertEqual('Не понял тип категории попробуйте снова.', answer)
