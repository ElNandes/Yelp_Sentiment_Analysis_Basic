import numpy as np
import pandas as pd
from base import SentimentAnalysis
from webscraper import WebScraper


class Yelp:

    def __init__(self, model_name, link, regular_expression):
        self.sa = SentimentAnalysis(model_name)
        self.ws = WebScraper(link, regular_expression)

    def sentiment_output(self, no_of_tokens = 512):
        review = self.ws.scraper()
        df = pd.DataFrame(np.array(review), columns=['review'])

        df['sentiment'] = df['review'].apply(lambda x: self.sa.sentiment_score(x[:no_of_tokens]))

        return df


def __main__():
    model_name = 'nlptown/bert-base-multilingual-uncased-sentiment'
    yelp_link = 'https://www.yelp.com/biz/social-brew-cafe-pyrmont'
    regular_expression = '.*comment.*'
    yelp = Yelp(model_name, yelp_link, regular_expression)
    sentiments = yelp.sentiment_output()

    print(sentiments)

__main__()
