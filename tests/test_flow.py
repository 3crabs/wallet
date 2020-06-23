import unittest

from Database import Database


class TestFlow(unittest.TestCase):

    def setUp(self) -> None:
        self.session = Database.new_base().session()
