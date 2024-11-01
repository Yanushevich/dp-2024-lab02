from handlers import message_formatter, log_handler
from logger import singleton_logger, log_level

if __name__ == "__main__":
    """Создание объекта логгера"""
    logger = singleton_logger.Logger()

    """Логи в консоль"""
    logger.set_log_output(log_handler.ConsoleLogHandler())
    logger.log(log_level.LogLevel.INFO, "Test message")

    """Замена вывода на файл"""
    logger.set_log_output(log_handler.FileLogHandler("./logs"))
    logger.log(log_level.LogLevel.INFO, "Test message")

    """Замена формата сообщения на верхний регистр"""
    logger.set_format(message_formatter.UpperLogMessage())
    logger.log(log_level.LogLevel.INFO, "Test message")

    """Логировать снова в консоль"""
    logger.set_log_output(log_handler.ConsoleLogHandler())
    logger.log(log_level.LogLevel.INFO, "Test message")
