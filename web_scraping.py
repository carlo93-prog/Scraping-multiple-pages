# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:34:20 2020

@author: carlo
"""

from bs4 import BeautifulSoup
import requests
import pprint

#%%
res=requests.get("https://news.ycombinator.com/news?p=")
soup= BeautifulSoup(res.text, "html.parser")
links=soup.select(".storylink")
subtext=soup.select(".subtext")

#%%
def sort_stories_by_votes(hnlist):
   return sorted(hnlist, key=lambda k:k['Votes'],reverse=True)


#%%
def create_custom_hn(links,subtext):
    hn=[]
    for page in range(1,20):      # Number of pages plus one 
        res=requests.get("https://news.ycombinator.com/news?p=" + format(page))
        soup= BeautifulSoup(res.text, "html.parser")
        links=soup.select(".storylink")
        subtext=soup.select(".subtext")
        for index,item in enumerate(links):
            title=item.getText()
            href=item.get("href",None)
            vote= subtext[index].select(".score")
            if len(vote):
                points=vote[0].getText().replace(' points', ' point')
                point= int(points.replace(' point', ''))
                if point >99:
                    hn.append({"Title":title, "Link":href, 'Votes': point})
              
    return sort_stories_by_votes(hn)

#%%
pprint.pprint(create_custom_hn(links,subtext))
