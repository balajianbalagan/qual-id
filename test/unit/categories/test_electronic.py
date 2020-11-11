import unittest
from qual_id.categories.electronic import Electronic
from test.unit.utils.category_helper import CategoryHelper


class TestElectronic(unittest.TestCase):
    def setUp(self):
        self.electronic = Electronic()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.electronic)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
