import threading
import log_handler


class Singleton:
    _instance = None
    _writer_lock = threading.Lock()
    _creator_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._creator_lock:
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Logger(Singleton):
    def __init__(self, handler: log_handler.LogHandler):
        self.log_handler = handler

    def log(self, message: str):
        with self._writer_lock:
            self.log_handler.log(message)
