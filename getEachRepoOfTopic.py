def get_topic_page(topic_url):
  response = requests.get(topic_url)
  if response.status_code != 200:
    raise Exception('Failed to load page {}'.format(topic_url))
  
  topic_soup = BeautifulSoup(response.text,'html.parser')
  return topic_soup

def get_repo_info(repo_tags,star_tag):
    #return all information required
    a_tags = repo_tags.find_all('a')
    username = a_tags[0].text.strip()
    repo_name = a_tags[1].text.strip()
    repo_url =  base_url + a_tags[1]['href']
    star = star_tag.text.strip()
    return username,repo_name,star,repo_url

def get_topic_repo(topic_soup):
  repo_tags = topic_soup.find_all("h3", {"class": "f3 color-fg-muted text-normal lh-condensed"})
  star_tag = topic_soup.find_all('span',{"class":"Counter js-social-count"})

  topic_repos_dict = {
    'username': [],
    'repo_name':[],
    'stars':[],
    'repo_url':[]
  }

  for i in range(len(repo_tags)):
    repo_info = get_repo_info(repo_tags[i],star_tag[i])
    topic_repos_dict['username'].append(repo_info[0])
    topic_repos_dict['repo_name'].append(repo_info[1])
    topic_repos_dict['stars'].append(repo_info[2])
    topic_repos_dict['repo_url'].append(repo_info[3])
    
  return pd.DataFrame(topic_repos_dict)
  
  
#get url from Topics or enter your url
url = topic_url[1]
repos = get_topic_repo(get_topic_page(url4))

#converting df to csv
repos.to_csv("repo.csv")
