import pandas as pd
import snscrape.modules.twitter as sntwitter

tmax = 1000000
tlist = []
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('jeffrey dahmer since:2016-01-01 until:2022-09-29').get_items()):
    if i>tmax:
        break
tlist.append([tweet.date, tweet.id, tweet.content, tweet.username])
tweets_df2 = pd.DataFrame(tlist, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
tweets_df2.to_csv("JefferyDahmer.csv", index = False)