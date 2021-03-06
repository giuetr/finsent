# finsent
Extract sentiment from financial news headlines for every US public company

------------- 

**Finsent** is a fast and seamless way to collect, classify and visualize sentiment polarity of financial news headlines for every US listed company.


Requirements:
------------- 
- requests
- BeautifulSoup
- nltk
- Vader Corpus

Running:
------------- 

The app uses a series of methods to perform different analysis and classification actions:

**1. news_sent:**
A method that creates a DataFrame of all the headlines for a specific company and a classification of sentiment polarity. Just feed it a ticker and the df will be created:

```bash
#We define the ticker (Oracle Corp.):
ticker = 'ORCL'
#And call the method:
headlines_df = finsent(ticker).news_sent()
headlines_df
```

**2. sentiment:**
A method that returns the aggregated sentiment of a given company:

```bash
#We define the ticker (Adobe Inc.):
ticker = 'ADBE'
#And call the method:
sentiment_df = finsent(ticker).sentiment()
sentiment_df
```

**3. get_all_stocks:**
A method that returns a DataFrame with sentiment polarity scores for a given array of tickers:

```bash
#We define a list of tickers:
tickers = ['F','AMD','NVDA','MU','FB','AMZN']

#And call the method:
sentiment_companies = finsent.get_all_stocks(tickers)
sentiment_companies
```
Output:

![](https://github.com/giuetr/finsent/blob/master/assets/sample.png)

The script took circa 2 seconds to capture and classify the sentiment embedded in over 600 key news headlines for a set of 6 companies, providing a convenient and time-efficient solution for a highly time-consuming practice.

 ------------- 

Enjoy!

License:
-------------

GNU General Public License v3.0

Copyright © 2019 giuetr

