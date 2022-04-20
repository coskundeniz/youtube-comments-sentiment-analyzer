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

    dataframe["Cleaned Comment Text"] = (
        dataframe["Original Comment Text"]
        # remove whitespace
        .str.strip()
        # replace newlines with space
        .str.replace("\n", " ")
        # remove mentions and links
        .str.replace(r"(?:\@|http?\://|https?\://|www)\S+", "", regex=True)
        # remove punctuations, emojis, special characters
        .str.replace(r"[^\w\s]+", "", regex=True)
        # turn into lowercase
        .str.lower()
        # remove numbers
        .str.replace(r"\d+", "", regex=True)
        # remove hashtags
        .str.replace(r"#\S+", " ", regex=True)
    )

    # remove stop words
    stop_words = stopwords.words("english")
    dataframe["Cleaned Comment Text"] = dataframe["Cleaned Comment Text"].apply(
        lambda comment: " ".join([word for word in comment.split() if word not in stop_words])
    )

    return dataframe
