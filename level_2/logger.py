"""
Дзен Пайтона
import this

LOGURU - альтернатива

"""
# import this
import logging
from logging.handlers import TimedRotatingFileHandler


def setup_debug_logger():
    debug_logger = logging.getLogger("debug_logger")
    debug_logger.setLevel(logging.DEBUG)

    debug_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - [%(levelname)s] - %(module)s:%(lineno)d - %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(debug_formatter)

    debug_logger.addHandler(console_handler)

    return debug_logger


def setup_error_logger():
    error_logger = logging.getLogger("error_logger")
    error_logger.setLevel(logging.ERROR)

    error_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - [%(levelname)s] - %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(error_formatter)

    file_handler = TimedRotatingFileHandler(
        "error_logs.log",
        when="midnight",
        interval=1,
        backupCount=20,
        encoding="utf-8"
    )
    file_handler.setFormatter(error_formatter)

    error_logger.addHandler(console_handler)
    error_logger.addHandler(file_handler)

    return error_logger


debug_logger = setup_debug_logger()
error_logger = setup_error_logger()

if __name__ == "__main__":
    debug_logger.debug("Это сообщение уровня DEBUG.")
    debug_logger.info("Информационное сообщение.")
    debug_logger.warning("Это предупреждение.")

    error_logger.error("Ошибка: что-то пошло не так!")
    error_logger.critical("Критическая ошибка!")
