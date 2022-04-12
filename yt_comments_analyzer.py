from argparse import ArgumentParser

from exceptions import YTCommentsAnalyzerException
from utils import logger
from youtube_service import YoutubeService


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

    for i, comment in enumerate(all_comments, start=1):
        print(f"{i}. {comment}\n")


if __name__ == "__main__":

    arg_parser = get_arg_parser()
    args = arg_parser.parse_args()

    try:
        main(args)

    except KeyboardInterrupt:
        logger.info("Program ended manually.")
