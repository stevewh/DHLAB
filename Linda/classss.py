#!/usr/bin/env python
# coding: utf-8

# In[40]:


class epitaph():
    def __init__(self, url = None, Id = None, date = 0, interpretative = None, language = None): 
     self.url = url
     self.Id = Id
     self.date = 0
     self.interpretative = interpretative
     self.language = language


# In[42]:


url = 'https://edh-www.adw.uni-heidelberg.de/edh/inschrift/HD000042&lang=en'


# In[43]:


def loadId():   
    if Id != None:
        print(Id)
    if Id == None: 
        print('no Id to load')
        
def loadinterpretative():
    interpretative != None
    
def languagefunction():
    if language != None:
        print(language)


# In[44]:


loadId()


# In[ ]:




