#Finsent core
#Finsent 1.0: a script for newsheadlines sentiment analysis on single or multiple stocks
#by giuetr ¤¤¤

#Calling the necessary libraries

import requests
import urllib.request
import pandas as pd
import json
from pandas.io.json import json_normalize
import time
from datetime import date
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class finsent:
    def __init__(self, ticker):
        self.ticker = ticker

    #URL generating function:
    def ticker_feed(self):
        url = "https://finviz.com/quote.ashx?t="+str(self.ticker)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news = soup.findAll('a',attrs={'class':'tab-link-news'})
        return news
    
    #Function that returns a list of headlines for a specific ticker:
    def parser(self):
        news_txt = []
        news = self.ticker_feed()
        for i in news:
            news_txt.append(i.text)
        return news_txt
    
    #We define a DataFrame of headlines and we assess the sentiment for each
    def news_sent(self):
        headlines = self.parser()
        df = pd.DataFrame(data={"Ticker": self.ticker, "Headline": headlines})
        sia = SentimentIntensityAnalyzer()
        output = []
        for i in headlines:
            pol_score = sia.polarity_scores(i)
            output.append(pol_score)
        output = json_normalize(output)
        df_hdln = pd.DataFrame(data={"Ticker":self.ticker, "Headline": headlines})
        df_output = pd.concat([df_hdln,output], axis=1,sort=False)
        return df_output
    
    #This method returns the aggregated sentiment value of the reference company:
    def get_averages(self):
        base_df = self.news_sent()
        averages = base_df.mean()
        avg_df = pd.DataFrame(data=averages).T
        return avg_df
    
    #Method to build the df of a company's aggregated sentiment:
    def sentiment(self):
        ticker = self.ticker
        sentiment = self.get_averages()
        #sentiment['Ticker']=ticker
        sentiment.insert(0,'Ticker',ticker)
        return sentiment
    

    #Method to build a df of all the companies in a specified list of tickers:
    def get_all_stocks(tickers):
        today = date. today()
        start = time.time()
        main = pd.DataFrame()
        for i in tickers:
            x = finsent(i)
            y = x.sentiment()
            main = main.append(y, ignore_index=True)
        end = time.time()
        print("Date:", today)
        print("Stocks analyzed: ", len(tickers))
        print("Execution time: ", end - start)
        return main
        
    
    
    