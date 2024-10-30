from abc import ABC, abstractmethod


class MessageFormatter(ABC):
    @staticmethod
    def format_message(message: str) -> str:
        pass


class InitialLogMessage(MessageFormatter):
    """Оставить сообщение не меняя регистр"""

    @staticmethod
    def format_message(message: str) -> str:
        return message


class UpperLogMessage(MessageFormatter):
    """Приведение сообщения к верхнему регистру"""

    @staticmethod
    def format_message(message: str) -> str:
        return message.upper()
