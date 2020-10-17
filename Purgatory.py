#!/usr/bin/env python
# coding: utf-8

# In[6]:


import CA_Assmb.json


# In[5]:


ls


# In[27]:


print (CA_Assmb)


# In[9]:


print (CA_Assmb.json)


# In[10]:


pwd


# In[11]:


import pandas


# In[12]:


import pandas as pd


# In[15]:


ca_as = pd.read_file(../data/CA_Assmb.json)


# In[16]:


import geopandas as gps


# In[17]:


read (CA_Assmb.json)


# In[18]:


read.json (CA_Assmb.json)


# In[19]:


read.file(CA_Assmb.json)


# In[20]:


print (CA_Assmb)


# In[21]:


print (CA_Assmb.json)


# In[22]:


import geopandas as gp


# In[23]:


Ass = gp.read_file(CA_Assmb.json)


# In[24]:


naleo = gp.read_file(naleo2019.csv)


# In[26]:


naleo = gp.read_file(naleo.org/wp-content/uploads/2019/12/NALEO_2019_Excel_Database.xlsx)


# In[28]:


naleo = naleo2019.csv


# In[1]:


Ass = gp.read_file('CA_Assmb.json')


# In[2]:


import geopandas as gp


# In[3]:


Ass = gp.read_file('CA_Assmb.json')


# In[4]:


naleo = gp.read_file('naleo2019.csv')


# In[5]:


import fiona


# In[6]:


Ass = gp.read_file('CA_Assmb.json')


# In[7]:


shape (naleo)


# In[8]:


gp.shape (naleo)


# In[9]:


naleo.shape


# In[10]:


naleo.info


# In[11]:


naleo.head


# In[12]:


naleo.info()


# In[13]:


naleo.info


# In[17]:


naleo ['POLITICALPARTY']


# In[18]:


naleo [POLITICALPARTY].value_counts()


# # naleo ['POLITICALPARTY'].value_counts()

# In[20]:


naleo ['POLITICALPARTY'].value_counts().plot.bar()


# In[28]:


naleo[['STATE', 'FIRST_NAME','LAST_NAME','TITLE','JURISDICTION', 'CITY','POLITICALPARTY']]


# In[29]:


desired_columns = ['STATE', 'FIRST_NAME','LAST_NAME','TITLE','JURISDICTION', 'CITY','POLITICALPARTY']


# In[31]:


naleo[desired_columns]


# In[32]:


neatnaleo = naleo[desired_columns]


# In[33]:


print (neatnaleo)


# In[34]:


neatnaleo


# In[37]:


neatnaleo[naleo.STATE == 'CA']


# In[39]:


for index, row in neatnaleo.iterrows()
    print (row.TITLE)


# In[ ]:




