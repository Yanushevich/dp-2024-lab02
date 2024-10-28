import os
import create_message
import message_formatter
import singleton_logger
import log_level
import log_handler

if __name__ == '__main__':
    """Логи в файл"""
    file_logger = singleton_logger.Logger(log_handler.FileLogHandler('./logs'))
    file_logger.log(
        message_formatter.UpperLogMessage().format_message(
            create_message.CreateMessage(log_level.LogLevel.INFO,'Logging to file in upper case')
        )
    )
    file_logger.log(
        message_formatter.InitialLogMessage().format_message(
            create_message.CreateMessage(log_level.LogLevel.INFO, 'Logging to file in initial case')
        )
    )
    """Логи в консоль"""
    console_logger = singleton_logger.Logger(log_handler.ConsoleLogHandler())
    console_logger.log(
        message_formatter.InitialLogMessage().format_message(
            create_message.CreateMessage(log_level.LogLevel.INFO, 'Logging to console in initial case')
        )
    )
    console_logger.log(
        message_formatter.UpperLogMessage().format_message(
            create_message.CreateMessage(log_level.LogLevel.INFO, 'Logging to console in upper case')
        )
    )
