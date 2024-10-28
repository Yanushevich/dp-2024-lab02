from datetime import datetime
import log_level


class CreateMessage(str):
    """Создание сообщения"""
    def __new__(cls, level: log_level.LogLevel, message: str):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return super().__new__(cls, f"{timestamp} [{level.value}] {message}\n")
