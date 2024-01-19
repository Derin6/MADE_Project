#!/usr/bin/env python
# coding: utf-8

# In[66]:


import pandas as pd
import sqlite3
import urllib.request
import requests
import io 
import urllib3
import zipfile



# In[67]:


def extract(url):
    header = {
  "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
        
  "X-Requested-With": "XMLHttpRequest"
}
    r = requests.get(url, headers=header)
    return r
    


# In[68]:


url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"


# In[90]:


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


# In[91]:


df.info()


# In[92]:


df2= df.iloc[:,[0,1,2,3,4,9,10]]


# In[93]:


df2.info()


# In[94]:


df2 = df2.rename(columns={'Batterietemperatur in °C': 'Batterietemperatur', 'Temperatur in °C (DWD)': 'Temperatur'})


# In[95]:


df2


# In[96]:


df3 = df2


# In[97]:


df3["Temperatur"].replace(',','.',regex=True,inplace=True)
df3["Batterietemperatur"].replace(',','.',regex=True,inplace=True)


# In[98]:


df3


# In[99]:


df3["Temperatur"] = df3["Temperatur"].astype(float)*9/5+32
df3["Batterietemperatur"] = df3["Batterietemperatur"].astype(float)*9/5+32


# In[100]:


df3


# In[101]:


(df3['Geraet'].astype(int) > 0).all()



# In[102]:


df3.info()


# In[103]:


conn = sqlite3.connect('temperatures.sqlite')
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




