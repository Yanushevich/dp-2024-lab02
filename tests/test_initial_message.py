import unittest
from handlers import message_formatter


class TestInitialMessage(unittest.TestCase):
    def setUp(self):
        self.message = "Initial Message"

    def test_if_initial(self):
        """Проверка: осталась ли строка в первоначальном виде"""
        formatted_message = message_formatter.InitialLogMessage().format_message(
            self.message
        )
        self.assertEqual(self.message, formatted_message)


if __name__ == "__main__":
    unittest.main()
