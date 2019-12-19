#!/usr/bin/env python
# coding: utf-8

# I tried to think about useful classes for my project. I put them all in this file. I am not sure that this is what was required, so in case I will implement it and upload it again. Thank you.

# In[ ]:


class epitaph():
    def __init__(self, url = None, Id = None, date = 0, interpretive = None, language = None): 
        self.url = url
        self.Id = Id
        self.date = 0
        self.interpretive = interpretive
        self.language = language


# In[ ]:


class spreadsheetepitaph(): #these variables could help defining the parameters of the spreadsheet (id + interpretive transcription + daterange)
    def _initi_(self, id, interpretive, date):
        self.id = id
        self.interpretive = interpretive
        self.date = date


# In[ ]:


class daterange(): #the date is a range, so defined by two numbers (start and end of the esteemed period)
    def _init_(self, id, start, end,):
        self.id = id
        self.start = start
        self.end = end


# In[ ]:


class tagnames(): #for tagging names I need the ID of the epitaph, the transcription and the three names
    def _init_(self, id, interpretive, nomen = None, praenomen = None, cognomen = None): #i set a default value for the names because some inscriptions may only have one or two names
        self.id = id
        self.interpretive = interpretive
        self.nomen = nomen
        self.praenomen = praenomen
        self.cognomen = cognomen


# In[ ]:


class namesbehaviour():
    def _init_(self, numberofnames = 0, daterange):
        self.numberofnames = 0
        self.daterange = daterange

