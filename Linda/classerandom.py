#!/usr/bin/env python
# coding: utf-8

# In[77]:


class box: 
    shape = None 
    lati = '' #numero di lati
    colour = None
    interno = '' #what's inside of the box


# In[78]:


def _init_(self, shape):
    self.shape = None
    
def setColour(self, colourone, colourtwo):
    self.colour = (colourone, colourtwo)
    
def getColourone(self):
    return self.colour[0]

def getColourtwo(self):
    return self.colour[1]
    
def setLati(self, lati):
    self.lati = lati
    
def setInterno(self, interno):
    self.interno = interno


# In[79]:


giftbox = box()


# In[83]:


giftbox.interno = 'Book'
giftbox.colour = 'white', 'red'


# In[84]:


giftbox.interno


# In[86]:


getColourone(giftbox)


# In[ ]:





# In[ ]:




