import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

from utils import logger

nltk.download("vader_lexicon", quiet=True)


def create_dataframe_from_comments(all_comments: list) -> pd.DataFrame:
    """Create a dataframe from comments

    :type all_comments: list
    :param all_comments: List of comments
    :rtype: pd.DataFrame
    :returns: Pandas dataframe
    """

    df = pd.DataFrame(list(all_comments), columns=["Original Comment Text"])

    return df


def analyze_comments(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Analyze comments by calculating polarity scores

    Add Sentiment Score and Sentiment columns to the dataframe.

    :type dataframe: pd.DataFrame
    :param dataframe: Comments dataframe
    :rtype: pd.DataFrame
    :returns: Dataframe with sentiment analysis results
    """

    logger.info("Performing sentiment analysis on comments...")

    analyzer = SentimentIntensityAnalyzer()

    dataframe["Sentiment Score"] = dataframe["Cleaned Comment Text"].apply(
        lambda comment: _get_polarity_score(analyzer, comment)
    )

    dataframe["Sentiment"] = dataframe["Sentiment Score"].apply(
        lambda score: _convert_score_to_sentiment(score)
    )

    return dataframe


def _get_polarity_score(analyzer: SentimentIntensityAnalyzer, text: str) -> float:
    """Calculate polarity score for the given text

    :type analyzer: SentimentIntensityAnalyzer
    :param analyzer: Sentiment analyzer for Vader model
    :type text: str
    :param text: Cleaned comment text
    :rtype: float
    :returns: Polarity score
    """

    scores = analyzer.polarity_scores(text)

    logger.debug(f"Text: {text}, Scores: {scores}")

    return scores["compound"]


def _convert_score_to_sentiment(score) -> str:
    """Convert score to sentiment

    :type score: float
    :param score: Polarity score
    :rtype: str
    :returns: Sentiment as Positive, Negative, or Neutral
    """

    sentiment = ""

    if score <= -0.5:
        sentiment = "Negative"
    elif -0.5 < score <= 0.5:
        sentiment = "Neutral"
    else:
        sentiment = "Positive"

    return sentiment
