from abc import ABC


class MessageFormatter(ABC):
    """Интерфейс для стратегии формата лога"""

    def format_message(self, message: str) -> str:
        """Форматирование лога по образцу"""
        pass


class InitialLogMessage(MessageFormatter):
    """Стратегия сохранения исходного формата"""

    def format_message(self, message: str) -> str:
        """Сохранение исходного формата"""
        return message


class UpperLogMessage(MessageFormatter):
    """Стратегия форматирования лога в верхний регистр"""

    def format_message(self, message: str) -> str:
        """Приведение сообщения к верхнему регистру"""
        return message.upper()
