import unittest
import os
from unittest import mock
from datetime import datetime
import log_handler


class TestFileCreation(unittest.TestCase):
    def setUp(self):
        """Название файла"""
        timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        self.file_name = f"DP.P1.{timestamp}.log"

    @unittest.mock.patch("builtins.open", new_callable=mock.mock_open)
    def test_file_creation(self, mock_open):
        """Проверка вызова функции создания файла"""
        log_handler.FileLogHandler("fake_path")
        mock_open.assert_called_once_with(os.path.join('fake_path', self.file_name), "w")

    @unittest.mock.patch("builtins.open", new_callable=mock.mock_open)
    def test_file_write(self, mock_open):
        """Проверка вызова функции открытия файла на добавление"""
        log_handler.FileLogHandler("fake_path").log("123")
        mock_open.assert_any_call(os.path.join('fake_path', self.file_name), "a")


if __name__ == "__main__":
    unittest.main()
