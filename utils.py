import json
import logging
from logging.handlers import RotatingFileHandler

# from exceptions import UnsupportedConfigFileError
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

    if not filename.endswith(".json"):
        # raise UnsupportedConfigFileError("Config file must be a json file!")
        pass

    with open(filename, encoding="utf-8") as configfile:
        config = json.load(configfile)

    return config


def create_dataframe_from_comments(all_comments: list) -> pandas.DataFrame:
    """Create a dataframe from comments

    :type all_comments: list
    :param all_comments: List of comments
    :rtype: pandas.DataFrame
    :returns: Pandas dataframe
    """

    df = pandas.DataFrame(list(all_comments), columns=["Original Comment Text"])

    # df.to_csv("comments_to_clean.csv", columns=["Original Comment Text"])

    # pandas.set_option("display.max_colwidth", None)
    # pandas.set_option("display.max_colwidth", 70)

    return df
