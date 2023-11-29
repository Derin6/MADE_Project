#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import requests


# In[74]:


data_url="https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"


# In[75]:


df= pd.read_csv(data_url,sep=';')


# In[76]:


df


# In[83]:


df.drop("Status",axis=1,inplace= True)


# In[64]:


Verkehr_list=("FV", "RV", "nur DPN")
df = df[df['Verkehr'].isin(Verkehr_list)]


# In[65]:


df.Laenge.replace(to_replace=",", value=".", inplace=True,regex=True)
df.Breite.replace(to_replace=",", value=".", inplace=True,regex=True)


# In[66]:


df = df.astype({'Laenge':'float'})
df = df.astype({'Breite':'float'})


# In[67]:


df


# In[68]:


df = df[(df.Laenge <= 90.0) & (df.Laenge >= -90.0)]


# In[98]:


df.dropna(inplace=True,)


# In[99]:


pattern = "^[A-Za-z]{2}:\d*:\d*(?::\d*)?$"


# In[101]:


df.IFOPT.str.match(pattern)


# In[103]:


df2=df[df.IFOPT.str.match(pattern)]


# In[104]:


df2


# In[105]:


import sqlite3


db_file_path = 'trainstops.sqlite'
conn = sqlite3.connect(db_file_path)

cursor = conn.cursor()

table_name = 'trainstops'
df2.to_sql(table_name, con=conn, if_exists='replace', index=False)

conn.commit()
conn.close()






# In[ ]:
