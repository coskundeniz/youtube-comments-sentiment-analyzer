class YTCommentsAnalyzerException(Exception):
    """Base exception for YouTube Comments Sentiment Analyzer"""


class MissingUrlError(YTCommentsAnalyzerException):
    """Missing video url exception"""
