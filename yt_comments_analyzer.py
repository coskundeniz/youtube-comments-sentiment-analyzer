from argparse import ArgumentParser

from data_cleaner import clean_comments
from exceptions import YTCommentsAnalyzerException
from utils import logger, create_dataframe_from_comments
from sentiment_analyzer import analyze_comments
from youtube_service import YoutubeService
from visualize import create_pie_chart


def handle_exception(exp: YTCommentsAnalyzerException) -> None:
    """Print the error message and exit

    :type exp: YTViewsTrackerException
    :param exp: Exception raised by the views tracker components
    """

    logger.error(exp)
    raise SystemExit() from exp


def get_arg_parser() -> ArgumentParser:
    """Get argument parser

    :rtype: ArgumentParser
    :returns: ArgumentParser object
    """

    arg_parser = ArgumentParser()
    arg_parser.add_argument("-u", "--url", help="Video URL to analyze comments")
    arg_parser.add_argument(
        "-o",
        "--output",
        default="sentiment_analysis_chart.png",
        help="Name or absolute path of the output chart",
    )
    arg_parser.add_argument(
        "-c", "--useconfig", action="store_true", help="Read configuration from config.json file"
    )
    arg_parser.add_argument(
        "-cf",
        "--configfile",
        default="config.json",
        help="Read configuration from given file",
    )
    arg_parser.add_argument(
        "-ir",
        "--include_replies",
        action="store_true",
        help="Include replies to top level comments",
    )

    return arg_parser


def main(args):
    """Entry point for the tool

    :type args: Namespace
    :pram args: Command line args returned by ArgumentParser
    """

    if not args.url:
        arg_parser.print_help()
        raise SystemExit("Missing url parameter!")

    service = YoutubeService(args.url, args.include_replies)

    all_comments = service.get_comment_threads()

    df = create_dataframe_from_comments(all_comments)

    logger.info("Cleaning data for analysis...")
    cleaned_df = clean_comments(df)

    results_df = analyze_comments(cleaned_df)

    print(results_df.head(30))

    video_title = service.get_video_title()
    create_pie_chart(results_df, video_title, args.output)


if __name__ == "__main__":

    arg_parser = get_arg_parser()
    args = arg_parser.parse_args()

    try:
        main(args)

    except KeyboardInterrupt:
        logger.info("Program ended manually.")
