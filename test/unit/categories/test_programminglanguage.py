import unittest
from qual_id.categories.programminglanguage import ProgrammingLanguage
from test.unit.utils.category_helper import CategoryHelper


class TestProgrammingLanguage(unittest.TestCase):
    def setUp(self):
        self.programminglanguage = ProgrammingLanguage()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(
            self.programminglanguage
        )
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
