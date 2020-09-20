import requests
from bs4 import BeautifulSoup
import pprint

url = 'https://news.ycombinator.com/'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.body.contents)
links = soup.select('.storylink')
votes = soup.select('.score')
subtext = soup.select('.subtext')
# for s in subtext:
    # print(s.find('span',attrs={'class':'score'} ).getText())

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'],reverse=True)

def create_custom_hn(links, subtext):
    hn = []

    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        # print(vote)
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title':title, 'link':href, 'votes': points})

    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))