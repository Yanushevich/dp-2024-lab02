import unittest
from unittest import mock
import io
from handlers import log_handler


class TestConsoleLog(unittest.TestCase):
    """Проверка вывода лога в консоль с использованием буфера"""

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_console_logging(self, mock_stdout):
        """Проверка вывода сообщения в консоль"""
        message = "Test printing message in console"
        logger = log_handler.ConsoleLogHandler()
        logger.log(message)
        self.assertEqual(mock_stdout.getvalue(), message)


if __name__ == "__main__":
    unittest.main()
