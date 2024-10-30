import threading
from handlers import message_formatter, log_handler
from logger import singleton


class Logger(singleton.Singleton):
    def __init__(self):
        self._writer_lock = threading.Lock()
        self._log_output = log_handler.ConsoleLogHandler()
        self._log_format = message_formatter.InitialLogMessage

    def set_log_output(self, handler: log_handler.LogHandler):
        self._log_output = handler

    def set_format(self, log_format: message_formatter.MessageFormatter):
        self._log_format = log_format

    def log(self, message: str):
        with self._writer_lock:
            self._log_output.log(self._log_format.format_message(message))
