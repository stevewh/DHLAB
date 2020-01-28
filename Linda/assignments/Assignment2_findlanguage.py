#!/usr/bin/env python
# coding: utf-8

# In[1]:


#load needed libraries
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd

# Create query variables
# base url string of site
urlBase = "https://edh-www.adw.uni-heidelberg.de"
# query parameters for the url, page size set to 100
urlQueryBase = "/inschrift/erweiterteSuche?hd_nr=&tm_nr=&beleg=c&land=&fo_antik=&fo_modern=&fundstelle=&region=&compFundjahr=eq&fundjahr=&aufbewahrung=&inschriftgattung=&sprache=L&inschrifttraeger=&compHoehe=eq&hoehe=&compBreite=eq&breite=&compTiefe=eq&tiefe=&bh=&palSchreibtechnik=&dat_tag=&dat_monat=&dat_jahr_a=&dat_jahr_e=&hist_periode=&religion=&literatur=&kommentar=&p_name=&p_praenomen=&p_nomen=&p_cognomen=&p_supernomen=&p_tribus=&p_origo=&p_geschlecht=&p_status=&compJahre=eq&p_lJahre=&compMonate=eq&p_lMonate=&compTage=eq&p_lTage=&compStunden=eq&p_lStunden=&atext1=&bool=AND&atext2=&beleg89=ja&nurMitFoto=ja&sort=hd_nr&anzahl=100&addFeldMaterial=ja&addFeldDTyp=ja&addFeldIGat=ja&start="
# offset of the query
offset = 0
# parameter to specify language as english
paramLang = "&lang=en"

#create query
url = urlBase + urlQueryBase + str(offset)
#print(url)


# In[2]:


#1. Load query results page
f = urllib.request.urlopen(url)
htmlDocString = f.read() 
f.close()
# take a quick look at the html
#print(htmlDocString)


# In[3]:


#2. Find a single result

#    - Create BeautifulSoup from result string
htmlSoup = BeautifulSoup(htmlDocString,'html.parser')
#print(htmlSoup.prettify())

#    - Get a list of all results reffer 'table' elements of class 'treffertabelle'
tableRefferList = htmlSoup.select('table.treffertabelle')
#print(type(tableRefferList)) #<class 'list'>
#print(len(tableRefferList))  #100

#set curTable to 3rd table scrap info for a single result while developing
#later this will just be a loop variable
curTable = tableRefferList[4]
#print (curTable.prettify())


# In[8]:


######################################################
## code to debug the "access denied" issue
######################################################
import requests
# inspect website to find particular item code
url = 'https://edh-www.adw.uni-heidelberg.de/edh/inschrift/HD000042&lang=en'

badresponse = requests.get(url) #access the website with requests library
#print (badresponse.text)
#print(badresponse.status_code)
#print ("-------------")

# spoofing user agent
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
goodresponse = requests.get(url, headers={"User-agent":user_agent}) #access the website with requests library
#print(goodresponse.status_code)

######################################################
## Code to understand what's bad with the html 
######################################################

from bs4 import BeautifulSoup
import requests

# inspect website to find particular item code
url = 'https://edh-www.adw.uni-heidelberg.de/edh/inschrift/HD000042&lang=en'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
response = requests.get(url, headers={"User-agent":user_agent}) #access the website with requests library

#parse HTML and save to BeautifulSoup object
bigsoup = BeautifulSoup(response.text, "html.parser")
## the html parser give a wrong html (check for</body></html> in wrong position)
#print ("--------------------------------------start------------------------------------")
#print(bigsoup)
#print ("--------------------------------------end------------------------------------")


######################################################
## the solution
######################################################

from bs4 import BeautifulSoup
import requests

# inspect website to find particular item code
url = 'https://edh-www.adw.uni-heidelberg.de/edh/inschrift/HD000042&lang=en'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
response = requests.get(url, headers={"User-agent":user_agent}) #access the website with requests library

#parse HTML and save to BeautifulSoup object
bigsoup = BeautifulSoup(response.text, "html.parser")

# no matter in what table, looking for <td>material</td> --> orginal is <td><b>material</b></td>
language = bigsoup.find('td', text='language').find_next('td')
print(language.text)


# In[ ]:




