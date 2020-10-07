import unittest
from qual_id.categories.scientist import Scientist
from test.utils.category_helper import CategoryHelper


class TestScientist(unittest.TestCase):
    def setUp(self):
        self.scientist = Scientist()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.scientist)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
