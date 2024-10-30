import threading
from datetime import datetime
from handlers import message_formatter, log_handler
from logger import singleton, log_level


class Logger(singleton.Singleton):
    def __init__(self):
        self.message = ""
        self._writer_lock = threading.Lock()
        self._log_output = log_handler.ConsoleLogHandler()
        self._log_format = message_formatter.InitialLogMessage()

    def _create_message(self, level: log_level.LogLevel, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.message = f"{timestamp} [{level.value}] {message}\n"

    def set_log_output(self, handler: log_handler.LogHandler):
        self._log_output = handler

    def set_format(self, log_format: message_formatter.MessageFormatter):
        self._log_format = log_format

    def log(self, level: log_level.LogLevel, message: str):
        self._create_message(level, message)
        with self._writer_lock:
            self._log_output.log(self._log_format.format_message(message=self.message))
