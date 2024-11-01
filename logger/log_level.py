from enum import Enum


class LogLevel(Enum):
    """Перечисление уровней логирования"""

    INFO = "INFO"
    TRACE = "TRACE"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"
