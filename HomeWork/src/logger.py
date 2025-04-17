import logging as log
from logging import Logger


def log_setup() -> Logger:
    """Настройки логгера."""
    logger = log.getLogger("masks")
    logger.setLevel(log.DEBUG)

    file_handler = log.FileHandler("code.log", "w", encoding="utf-8")
    formatter = log.Formatter("%(asctime)s - %(module)s, %(levelname)s: %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
