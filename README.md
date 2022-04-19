YouTube Comments Sentiment Analyzer
===================================

YouTube comments sentiment analyzer tool that makes polarity analysis.
The result is saved as a pie chart output.

---

## How to setup

* Run the following commands to install the required packages

    * `cd <project directory>`
    * `python -m venv env`
    * `source env/bin/activate`
    * `python -m pip install -r requirements.txt`

---

## How to use

```
usage: python yt_comments_analyzer.py [-h] [-u URL] [-c] [-cf CONFIGFILE] [-ir] [-o OUTPUT]

optional arguments:
  -h, --help                              show this help message and exit
  -u URL, --url URL                       Video URL to analyze comments
  -c, --useconfig                         Read configuration from config.json file
  -cf CONFIGFILE, --configfile CONFIGFILE Read configuration from given file
  -ir, --include_replies                  Include replies to top level comments
  -o OUTPUT, --output OUTPUT              Name or absolute path of the output chart
```

### Example Commands

* Get comments for the given video and output results to *sentiment_analysis_chart.png* file.
    * `python yt_comments_analyzer.py -u https://www.youtube.com/watch?v=mM2-FPm1EhI`

![Result 1](images/sentiment_analysis_chart_2.png)

* Get comments with replies for the given video and output results to *result_chart.png* file.
    * `python yt_comments_analyzer.py -u https://www.youtube.com/watch?v=ixzKvJeXrY4 -ir -o result_chart.png`

![Result 2](images/sentiment_analysis_chart_4.png)

* Get parameters from *config.json* file.
    * `python yt_comments_analyzer.py -c`

* Get parameters from the given config file.
    * `python yt_comments_analyzer.py -c -cf custom_config.json`

* Example video of an execution

[![Sample Execution](images/sentiment_analysis_chart_1.png)](https://www.youtube.com/watch?v=4BnxaXusG-g "YouTube Comments Sentiment Analyzer")
