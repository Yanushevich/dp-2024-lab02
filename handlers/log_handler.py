from abc import ABC, abstractmethod
import os
from datetime import datetime


class LogHandler(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass


class FileLogHandler(LogHandler):

    def __init__(self, folder_path: str):
        self.file_path = self.create_file(folder_path)

    @staticmethod
    def create_file(folder_path: str) -> str:
        """Создание файла"""
        timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        log_filename = f"DP.P1.{timestamp}.log"
        file_path = os.path.join(folder_path, log_filename)
        with open(file_path, "w"):
            pass
        return file_path

    def log(self, message: str) -> None:
        """Запись лога в файл"""
        with open(self.file_path, "a") as log_output:
            log_output.write(message)


class ConsoleLogHandler(LogHandler):
    """Вывод лога в консоль"""

    def log(self, message: str) -> None:
        print(message, end="")
