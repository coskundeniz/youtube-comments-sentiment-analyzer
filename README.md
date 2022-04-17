YouTube Comments Sentiment Analyzer
===================================

YouTube comments sentiment analyzer tool


* https://github.com/googleapis/google-api-python-client
* https://github.com/googleapis/google-api-python-client/blob/main/docs/README.md
* https://developers.google.com/youtube/v3/docs/comments

* https://machinelearningmastery.com/basic-data-cleaning-for-machine-learning/

---

* Data cleaning steps

    * Remove emojis +, URLs +, special characters +, and punctuation  +++
    * Convert all text to lowercase +++
    * Remove stop words: and, the, it, at, etc. +++
    * Correct abbreviated words

* https://towardsdatascience.com/part-1-data-cleaning-does-bert-need-clean-data-6a50c9c6e9fd
* https://stackoverflow.com/questions/66338970/cleaning-text-using-nltk

* Sentiment analysis

    * https://www.red-gate.com/simple-talk/development/data-science-development/sentiment-analysis-python/
    * https://textblob.readthedocs.io/en/latest/quickstart.html#sentiment-analysis
    * https://www.youtube.com/watch?v=ujId4ipkBio
    * https://www.youtube.com/watch?v=szczpgOEdXs
    * https://towardsdatascience.com/the-most-favorable-pre-trained-sentiment-classifiers-in-python-9107c06442c6

* YouTube Rewind 2019: For the Record --> 1,074,433 Comments
    * https://www.youtube.com/watch?v=2lAe1cqCOXo

* Call Of Duty Infinite Warfare - Game Movie --> 1,727 Comments
    * https://www.youtube.com/watch?v=ixzKvJeXrY4

* Official Reveal Trailer | Call of Duty: Infinite Warfare --> 743,563 Comments
    * https://www.youtube.com/watch?v=EeF3UTkCoxY


p yt_comments_analyzer.py -u https://www.youtube.com/watch?v=14z_Tf3p2Mw -o result_chart_final_5.png -ir

p yt_comments_analyzer.py -u https://www.youtube.com/watch?v=EeF3UTkCoxY -o result_chart_final_6.png


