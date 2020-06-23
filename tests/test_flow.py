import unittest

from Category import Category
from Database import Database
from TypeFlow import TypeFlow
from answer import text_answer


class TestFlow(unittest.TestCase):

    def setUp(self) -> None:
        self.session = Database.new_base().session()

    def test_add_flow_1000_bad_category_transport(self):
        answer = text_answer('Wallet добавь 1000 в транспорт')
        self.assertEqual('Категория транспорт не найдена', answer)

    def test_add_flow_1000_category_transport(self):
        self.session.add(Category('транспорт', TypeFlow.LESS))
        self.session.commit()
        answer = text_answer('Wallet добавь 1000 в транспорт')
        self.assertEqual('В транспорт добавлена 1000р!', answer)

    def test_add_flow_1000_category_work(self):
        self.session.add(Category('работа', TypeFlow.PROFIT))
        self.session.commit()
        answer = text_answer('Wallet добавь 1000 в работа')
        self.assertEqual('В работа добавлена 1000р!', answer)

    def test_add_flow_2000_category_transport(self):
        self.session.add(Category('транспорт', TypeFlow.LESS))
        self.session.commit()
        answer = text_answer('Wallet добавь 2000 в транспорт')
        self.assertEqual('В транспорт добавлена 2000р!', answer)
