#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Untitled444


# In[2]:


import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests


# In[3]:


url = 'https://edh-www.adw.uni-heidelberg.de/edh/inschrift/HD000042&lang=en'


# In[4]:


Untitled444.findTypeofinscription(url)


# In[6]:


Untitled444.findTypeofmonument(url)


# In[7]:


Untitled444.findMaterial(url)


# In[ ]:




