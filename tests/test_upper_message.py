import unittest
from handlers import message_formatter


class TestUpperMessage(unittest.TestCase):
    """Проверка стратегии формата верхнего регистра"""

    def setUp(self):
        """Первоначальное сообщение"""
        self.message = "Not Upper case message"

    def test_if_upper(self):
        """Проверка: стала ли строка в верхнем регистре"""
        new_message = message_formatter.UpperLogMessage().format_message(self.message)
        self.assertTrue(new_message.isupper())


if __name__ == "__main__":
    unittest.main()
