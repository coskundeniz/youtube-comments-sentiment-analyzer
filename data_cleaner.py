import nltk
from nltk.corpus import stopwords
import pandas as pd

nltk.download("stopwords")


def clean_comments(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Perform data cleaning on comments to prepare for analysis

    :type dataframe: pd.DataFrame
    :param dataframe: Uncleaned dataframe for comments
    :rtype: pd.DataFrame
    :returns: Cleaned pandas dataframe
    """

    cleaned_df = dataframe.copy()

    # remove whitespace
    cleaned_df["Original Comment Text"] = cleaned_df["Original Comment Text"].str.strip()

    # replace newlines with space
    cleaned_df["Original Comment Text"] = cleaned_df["Original Comment Text"].str.replace("\n", " ")

    # remove mentions and links
    cleaned_df["Original Comment Text"] = cleaned_df["Original Comment Text"].str.replace(
        r"(?:\@|http?\://|https?\://|www)\S+", "", regex=True
    )

    # remove punctuations, emojis, special characters
    cleaned_df["Original Comment Text"] = cleaned_df["Original Comment Text"].str.replace(
        r"[^\w\s]+", "", regex=True
    )

    # turn to lowercase
    cleaned_df["Original Comment Text"] = cleaned_df["Original Comment Text"].str.lower()

    # remove numbers
    cleaned_df["Original Comment Text"] = cleaned_df["Original Comment Text"].str.replace(
        r"\d+", "", regex=True
    )

    # remove stop words
    stop_words = stopwords.words("english")
    cleaned_df["Original Comment Text"] = cleaned_df["Original Comment Text"].apply(
        lambda x: " ".join([word for word in x.split() if word not in stop_words])
    )

    return cleaned_df
