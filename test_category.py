import unittest

from answer import text_answer


class MyTestCase(unittest.TestCase):

    def test_add_category(self):
        answer = text_answer('Wallet добавь категорию транспорт')
        self.assertEqual('Категория транспорт добавлена!', answer)


if __name__ == '__main__':
    unittest.main()
