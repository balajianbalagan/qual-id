import unittest
from qual_id.categories.fruit import Fruit
from test.utils.category_helper import CategoryHelper


class TestFruit(unittest.TestCase):
    def setUp(self):
        self.fruit = Fruit()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.fruit)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
