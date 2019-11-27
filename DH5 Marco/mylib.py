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
    return bigsoup
    #print(bigsoup.prettify())    #if you want to see the results, then delete that #

def findMaterial(url):
    bigsoupRet = soupify(url)
    material = bigsoupRet.find('td', text='material').find_next('td')
    print(material.text)

