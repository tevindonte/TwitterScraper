import twint
import pandas


print ("Fetching Tweets")

#Configure
config = twint.Config()
config.Search = "Jeffery Dahmer" #Search terms
config.Lang = "en" #Compatible language
config.Pandas = True #Enable Pandas integration.
config.Limit = 100000 #Number of Tweets to pull
config.Since = "2019–04–29" #Filter Tweets sent since date, works only with twint.run.Search (Example: 2017-12-27).
config.Until = "2022–09–29" #Filter Tweets sent until date, works only with twint.run.Search (Example: 2017-12-27).
config.Store_csv=True #Set to True to write as a csv file.
config.Output = "jefferydahm.csv" #Name of the output file.
twint.run.Search(config)

print('Scraping Done!')

