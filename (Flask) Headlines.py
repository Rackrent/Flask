import feedparser
from flask import Flask
app = Flask(__name__)
bbc_feed = 'http://feeds.bbci.co.uk/news/rss.xml'

@app.route("/")
def get_news():
    feed = feedparser.parse(bbc_feed)
    first_article= feed['entries'][0]
    return """<html>
    <body>
    <h1> This is the recent news </h1>
    <b>{0}</b><br/>
    <i>{1}</i><br/>
    <p<{2}</p><br/>
    </body>
    </html>""".format(first_article.get("title"),first_article.
    get("published"), first_article.get("summary"))
if __name__ == "__main__":
        app.run(port=5000, debug= True)
