from argparse import ArgumentParser

from data_cleaner import clean_comments
from utils import logger, get_configuration
from sentiment_analyzer import create_dataframe_from_comments, analyze_comments
from youtube_service import YoutubeService
from visualize import create_pie_chart


def get_arg_parser() -> ArgumentParser:
    """Get argument parser

    :rtype: ArgumentParser
    :returns: ArgumentParser object
    """

    arg_parser = ArgumentParser()
    arg_parser.add_argument("-u", "--url", help="Video URL to analyze comments")
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
    arg_parser.add_argument(
        "-o",
        "--output",
        default="sentiment_analysis_chart.png",
        help="Name or absolute path of the output chart",
    )

    return arg_parser


def main():
    """Entry point for the tool"""

    try:
        arg_parser = get_arg_parser()
        args = arg_parser.parse_args()

        if not (args.url or args.useconfig):
            arg_parser.print_help()
            raise SystemExit("Missing parameter!")

        config = get_configuration(args.configfile)

        video_url = config["url"] if args.useconfig else args.url
        include_replies = config["include_replies"] if args.useconfig else args.include_replies
        output_file = config["output"] if args.useconfig else args.output

        service = YoutubeService(video_url, include_replies)

        all_comments = service.get_comment_threads()

        df = create_dataframe_from_comments(all_comments)
        cleaned_df = clean_comments(df)
        results_df = analyze_comments(cleaned_df)

        video_title = service.get_video_title()

        create_pie_chart(results_df, video_title, output_file)

    except KeyboardInterrupt:
        logger.info("Program was ended manually.")


if __name__ == "__main__":

    main()
