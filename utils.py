import json
import logging
from logging.handlers import RotatingFileHandler

import pandas


LOG_FILENAME = "yt_comments_analyzer.log"

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(
    LOG_FILENAME, maxBytes=20971520, encoding="utf-8", backupCount=50
)
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
console_log_format = "%(asctime)s [%(levelname)5s] %(lineno)3d: %(message)s"
file_log_format = "%(asctime)s [%(levelname)5s] %(filename)s:%(lineno)3d: %(message)s"
console_formatter = logging.Formatter(console_log_format, datefmt="%d-%m-%Y %H:%M:%S")
console_handler.setFormatter(console_formatter)
file_formatter = logging.Formatter(file_log_format, datefmt="%d-%m-%Y %H:%M:%S")
file_handler.setFormatter(file_formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def get_configuration(filename="config.json") -> dict:
    """Read configuration file

    :type filename: str
    :param filename: Name of the configuration file
    :rtype: dict
    :returns: Configuration as dict
    """

    with open(filename, encoding="utf-8") as configfile:
        config = json.load(configfile)

    return config
