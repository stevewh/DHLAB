#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests

def soupify(url):     #first, bypasses security. Then creates Beautiful Soup with response
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    ingredients = requests.get(url, headers={"User-agent":user_agent}) #access the website with requests library
    bigsoup = BeautifulSoup(ingredients.text, "html.parser")
    print(bigsoup.prettify())    #if you want to see the results, then delete that #

def findLanguage(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    ingredients = requests.get(url, headers={"User-agent":user_agent}) #access the website with requests library
    bigsoup = BeautifulSoup(ingredients.text, "html.parser")
    thelanguage = bigsoup.find('td', text='language').find_next('td')
    print(thelanguage.text)

