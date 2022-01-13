pip install requests 
pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_all_topics():
  base_url = 'https://github.com/'
  topic_url = "/topics"
  page = requests.get(base_url+topic_url)

  topic_name = []
  topic_desc = []
  topic_url =[]

  soup = BeautifulSoup(page.text,'html.parser')
  topics = soup.find_all("div", {"class": "py-4 border-bottom d-flex flex-justify-between"})
  for topic in topics:
    topic_name.append(topic.find("p", {"class": "lh-condensed"}).text)
    topic_desc.append(topic.find("p", {"class": "color-fg-muted"}).text.lstrip())
    topic_url.append(base_url+topic.a.get('href'))

  mydataset = {
    'topic_name': topic_name,
    'topic_desc': topic_desc,
    'topic_url' : topic_url,
  }
  return pd.DataFrame(mydataset)

get_all_topics()
