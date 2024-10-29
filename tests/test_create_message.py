import unittest
import create_message
import log_level
from datetime import datetime


class TestCreateMessage(unittest.TestCase):
    def setUp(self):
        self.message = create_message.CreateMessage(log_level.LogLevel.INFO, "Testing")

    def test_message_type(self):
        """Проверка на тип созданного сообщения строке"""
        self.assertIsInstance(self.message, str)

    def test_message_content(self):
        """Сравнение сообщений, созданных классом и вручную"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_message = f"{timestamp} [INFO] Testing\n"
        self.assertEqual(self.message, new_message)


if __name__ == "__main__":
    unittest.main()
