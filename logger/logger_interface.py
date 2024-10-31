from abc import ABC, abstractmethod

from handlers import log_handler, message_formatter
from logger import log_level


class ILogger(ABC):
    """Интерфейс логгера"""

    @abstractmethod
    def set_log_output(self, handler: log_handler.LogHandler) -> None:
        """Устанавливает стратегию вывода лога."""
        pass

    @abstractmethod
    def set_format(self, log_format: message_formatter.MessageFormatter) -> None:
        """Устанавливает стратегию формата лога."""
        pass

    @abstractmethod
    def log(self, level: log_level.LogLevel, message: str) -> None:
        """Логирует сообщение с указанным уровнем."""
        pass
