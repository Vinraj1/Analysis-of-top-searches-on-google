import pandas as pd
from pytrends.request import TrendReq #pytrends only used for google trends data
import matplotlib.pyplot as plt
import time

Trending_topics = TrendReq(hl='en-US', tz=360) #Setting up language and timezone for google trends data

#Build Payload
kw_list=["Data Analytics"] #Searching for the term "Data Analytics" as a keyword
Trending_topics.build_payload(kw_list,cat=0, timeframe='today 12-m')
    #For the above trending topics we are using build_payload to search the keyword for all categories, for the past 12 months.
    #For the particular time_frame pattern used("today #-m") only 1, 3 and 12 months data can be acquired.

time.sleep(5) #providing delay for avoiding 429 Too Many Requests error from google trends

#Interest Over Time
data = Trending_topics.interest_over_time() #Returns the dataframe with the interest over time for the searched keyword
data = data.sort_values(by="Data Analytics", ascending = False)
data = data.head(10) #Top 10 results for the interest over time for the searched keyword
print(data)

#Historical Hour Interest
kw_list = ["Data Analytics"]
Trending_topics.build_payload(kw_list, cat=0, timeframe='2024-01-01 2024-02-01', geo='', gprop='')
data = Trending_topics.interest_over_time()
data = data.sort_values(by="Data Analytics", ascending = False)
data = data.head(10)
print(data)

#Interest By Region
data = Trending_topics.interest_by_region()
data = data.sort_values(by="Data Analytics", ascending = False)
data = data.head(10)
print(data)

#Visualizing Interest By Region
data.reset_index().plot(x='geoName', y='Data Analytics',figsize=(10,5), kind="bar")
plt.style.use('fivethirtyeight') #Specifies visual style for the plot
plt.show()

#Searching for Related Queries
try:
    Trending_topics.build_payload(kw_list=['Data Analytics'])
    related_queries = Trending_topics.related_queries() #interest_over_time() gives when people searched for the keyword,
    #Whereas related_queries() gives what other keywords people searched for along with the searched keyword.
    related_queries.values()
except (KeyError, IndexError):
    print("No related queries found for 'Data Analytics'")

#Keyword Suggestions
keywords = Trending_topics.suggestions(keyword='Data Analytics')
df = pd.DataFrame(keywords)
df.drop(columns= 'mid')