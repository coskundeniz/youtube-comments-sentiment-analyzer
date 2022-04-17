import os

import matplotlib.pyplot as plt

from utils import logger


def create_pie_chart(dataframe: "pandas.DataFrame", video_title: str, filename: str) -> None:
    """Create pie chart for the resulting analysis

    :type dataframe: pandas.DataFrame
    :param dataframe: Comments dataframe
    :type video_title: str
    :param video_title: Video title
    :type filename: str
    :param filename: Name or absolute path of the output chart
    """

    sentiment_counts_df = dataframe["Sentiment"].value_counts().to_frame()
    sentiment_counts_df.reset_index(inplace=True)
    sentiment_counts_df.rename(columns={"index": "Sentiment", "Sentiment": "Counts"}, inplace=True)

    sentiment_counts_df = sentiment_counts_df.set_index("Sentiment")

    axis = sentiment_counts_df.plot.pie(
        y="Counts",
        ylabel="",
        figsize=(12, 12),
        fontsize=15,
        autopct="%1.1f%%",
        startangle=90,
        legend=False,
        textprops={"color": "w", "weight": "bold"},
        colors=_get_colors(sentiment_counts_df),
    )

    plt.axis("equal")

    axis.set_facecolor("black")
    axis.set_title(
        f"Sentiment Analysis Results\n{video_title}",
        fontdict={"color": "white", "fontweight": "bold", "fontsize": 16},
        linespacing=2,
        pad=30,
    )

    figure = axis.get_figure()
    figure.savefig(filename, facecolor="black", dpi=600)

    logger.info(f"Output chart saved to {os.path.abspath(filename)}")


def _get_colors(sentiment_df: "pandas.DataFrame") -> list:
    """Get colors to use for chart

    :type sentiment_df: pandas.DataFrame
    :param sentiment_df: Comments dataframe
    :rtype: list
    :returns: List of color codes
    """

    number_of_sentiments = len(sentiment_df)

    blue = "#3385ff"
    green = "#00802b"
    red = "#80002a"
    orange = "#ff471a"

    if number_of_sentiments == 3:
        return [blue, green, red]

    return [orange, blue]
