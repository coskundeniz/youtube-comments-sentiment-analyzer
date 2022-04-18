import nltk
from nltk.corpus import stopwords
import pandas as pd

from utils import logger

nltk.download("stopwords", quiet=True)


def clean_comments(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Perform data cleaning on comments to prepare for analysis

    :type dataframe: pd.DataFrame
    :param dataframe: Uncleaned dataframe for comments
    :rtype: pd.DataFrame
    :returns: Cleaned pandas dataframe
    """

    logger.info("Cleaning data for analysis...")

    # remove whitespace
    dataframe["Cleaned Comment Text"] = dataframe["Original Comment Text"].str.strip()

    # replace newlines with space
    dataframe["Cleaned Comment Text"] = dataframe["Cleaned Comment Text"].str.replace("\n", " ")

    # remove mentions and links
    dataframe["Cleaned Comment Text"] = dataframe["Cleaned Comment Text"].str.replace(
        r"(?:\@|http?\://|https?\://|www)\S+", "", regex=True
    )

    # remove punctuations, emojis, special characters
    dataframe["Cleaned Comment Text"] = dataframe["Cleaned Comment Text"].str.replace(
        r"[^\w\s]+", "", regex=True
    )

    # turn to lowercase
    dataframe["Cleaned Comment Text"] = dataframe["Cleaned Comment Text"].str.lower()

    # remove numbers
    dataframe["Cleaned Comment Text"] = dataframe["Cleaned Comment Text"].str.replace(
        r"\d+", "", regex=True
    )

    # remove hashtags
    dataframe["Cleaned Comment Text"] = dataframe["Cleaned Comment Text"].str.replace(
        r"#\S+", " ", regex=True
    )

    # remove stop words
    stop_words = stopwords.words("english")
    dataframe["Cleaned Comment Text"] = dataframe["Cleaned Comment Text"].apply(
        lambda comment: " ".join([word for word in comment.split() if word not in stop_words])
    )

    return dataframe
