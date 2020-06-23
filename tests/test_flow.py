import unittest

from Database import Database
from answer import text_answer


class TestFlow(unittest.TestCase):

    def setUp(self) -> None:
        self.session = Database.new_base().session()

    def test_add_flow_1000_category_transport(self):
        answer = text_answer('Wallet добавь 1000 в транспорт')
        self.assertEqual('В транспорт добавлена 1000р!', answer)
