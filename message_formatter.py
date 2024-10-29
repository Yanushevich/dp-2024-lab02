from abc import ABC, abstractmethod


class FormatMessage(ABC):
    @abstractmethod
    def format_message(self, message: str) -> str:
        pass


class InitialLogMessage(FormatMessage):
    """Оставить сообщение не меняя регистр"""

    def format_message(self, message: str) -> str:
        return message


class UpperLogMessage(FormatMessage):
    """Приведение сообщения к верхнему регистру"""

    def format_message(self, message: str) -> str:
        return message.upper()
