import os

import matplotlib.pyplot as plt

from utils import logger


def create_pie_chart(dataframe: "pandas.DataFrame", filename: str) -> None:
    """Create pie chart for the resulting analysis

    :type dataframe: pandas.DataFrame
    :param dataframe: Comments dataframe
    :type filename: str
    :param filename: Name or absolute path of the output chart
    """

    sentiment_counts_df = dataframe["Sentiment"].value_counts().to_frame()
    sentiment_counts_df.reset_index(inplace=True)
    sentiment_counts_df.rename(columns={"index": "Sentiment", "Sentiment": "Counts"}, inplace=True)

    sentiment_counts_df = sentiment_counts_df.set_index("Sentiment")

    # if there is a missing sentiment, add it with value 0
    # sentiments = {"Positive", "Neutral", "Negative"}
    # missing_sentiment_set = sentiments - set(sentiment_counts_df["Sentiment"].to_list())
    # if missing_sentiment_set:
    #     missing_sentiment = missing_sentiment_set.pop()
    #     sentiment_counts_df.loc[len(sentiment_counts_df.index)] = [missing_sentiment, 0]

    axis = sentiment_counts_df.plot.pie(
        y="Counts",
        ylabel="",
        title="Sentiment Analysis Results",
        figsize=(12, 12),
        fontsize=15,
        autopct="%1.1f%%",
        startangle=90,
        legend=False,
        textprops=dict(color="w", weight="bold"),
        # colors=["lightgray", "green", "red"], # ["darkorange", "springgreen", "red"] -> output2
        # colors=["darkorange", "springgreen", "red"],
    )

    # plt.style.use("grayscale")  # output4.png

    plt.figure(facecolor="black")
    plt.axis("equal")

    figure = axis.get_figure()
    figure.savefig(filename, facecolor="black", transparent=True, dpi=600)

    logger.info(f"Output chart saved to {os.path.abspath(filename)}")
