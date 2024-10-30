import create_message
from handlers import message_formatter, log_handler
from logger import logger, log_level

if __name__ == "__main__":
    """Создание объекта логгера"""
    logger = logger.Logger()
    """Создание сообщения"""
    message = create_message.CreateMessage(log_level.LogLevel.INFO, "Test message")
    """Логи в консоль"""
    logger.set_log_output(log_handler.ConsoleLogHandler())
    logger.log(message)
    """Замена вывода на файл"""
    logger.set_log_output(log_handler.FileLogHandler("./logs"))
    logger.log(message)
    """Замена формата сообщения на верхний регистр"""
    logger.set_format(message_formatter.UpperLogMessage())
    logger.log(message)
    """Логировать снова в консоль"""
    logger.set_log_output(log_handler.ConsoleLogHandler())
    logger.log(message)
