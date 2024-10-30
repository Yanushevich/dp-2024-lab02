from abc import ABC


class MessageFormatter(ABC):

    def format_message(self, message: str) -> str:
        pass


class InitialLogMessage(MessageFormatter):
    """Оставить сообщение не меняя регистр"""

    def format_message(self, message: str) -> str:
        return message


class UpperLogMessage(MessageFormatter):
    """Приведение сообщения к верхнему регистру"""

    def format_message(self, message: str) -> str:
        return message.upper()
