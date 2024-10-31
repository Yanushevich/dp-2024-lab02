import unittest
from logger import log_level


class TestLogLevel(unittest.TestCase):
    """Проверка перечисления уровней логирования"""

    def test_level_values(self):
        """Проверка на соответствие значений названиям"""
        self.assertEqual(log_level.LogLevel.INFO.value, "INFO")
        self.assertEqual(log_level.LogLevel.TRACE.value, "TRACE")
        self.assertEqual(log_level.LogLevel.WARN.value, "WARN")
        self.assertEqual(log_level.LogLevel.ERROR.value, "ERROR")
        self.assertEqual(log_level.LogLevel.FATAL.value, "FATAL")


if __name__ == "__main__":
    unittest.main()
