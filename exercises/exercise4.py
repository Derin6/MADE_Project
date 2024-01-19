#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import sqlite3
from urllib.request import urlopen
import io 
import zipfile


# In[21]:


def extract(url):
    header = {
  "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
        
  "X-Requested-With": "XMLHttpRequest"
}
    r = urlopen(url)
    return r
    


# In[22]:


url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"


# In[23]:


zip_file = extract(url)
z = zipfile.ZipFile(io.BytesIO(zip_file.content))
z.extract("data.csv")

df = pd.read_csv("data.csv", sep=";",on_bad_lines='skip')
column_names = df.columns.values.tolist()

df = pd.read_csv('data.csv', sep='\t', header=None, names=['raw'], on_bad_lines='skip',skiprows=1)
df_split = df['raw'].str.split(';', expand=True,)
df= df_split.iloc[:,0:16]
expected_cols = 15  # change this to your actual number of columns
df.columns = column_names


# In[5]:


df.info()


# In[6]:


df2= df.iloc[:,[0,1,2,3,4,9,10]]


# In[7]:


df2.info()


# In[8]:


df2 = df2.rename(columns={'Batterietemperatur in °C': 'Batterietemperatur', 'Temperatur in °C (DWD)': 'Temperatur'})


# In[9]:


df2


# In[10]:


df3 = df2


# In[11]:


df3["Temperatur"].replace(',','.',regex=True,inplace=True)
df3["Batterietemperatur"].replace(',','.',regex=True,inplace=True)


# In[12]:


df3


# In[13]:


df3["Temperatur"] = df3["Temperatur"].astype(float)*9/5+32
df3["Batterietemperatur"] = df3["Batterietemperatur"].astype(float)*9/5+32


# In[14]:


df3


# In[15]:


(df3['Geraet'].astype(int) > 0).all()



# In[16]:


df3.info()


# In[19]:


conn = sqlite3.connect("temperatures.sqlite")
cursor = conn.cursor()

df_data_types = {
    'Geraet': 'BIGINT',
    'Hersteller': 'TEXT ',
    'Model' :'TEXT ',
    'Monat': 'BIGINT',
    'Temperatur': 'FLOAT' ,
    'Batterietemperatur': 'FLOAT',
    'Geraet aktiv': 'TEXT ',


    
    
}


df3.to_sql('temperatures', conn, if_exists='replace', index=False , dtype=df_data_types)


conn.commit()
conn.close()


# In[ ]:





# In[ ]:




