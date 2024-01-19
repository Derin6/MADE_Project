#!/usr/bin/env python
# coding: utf-8

# In[131]:


import pandas as pd
import sqlalchemy
import urllib.request
import requests
import io 
import ssl
import urllib3
import zipfile

ssl._create_default_https_context = ssl._create_unverified_context


# In[132]:


class CustomHttpAdapter (requests.adapters.HTTPAdapter):
    # "Transport adapter" that allows us to use custom ssl_context.

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)


def get_legacy_session():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
    session = requests.session()
    session.mount('https://', CustomHttpAdapter(ctx))
    return session


# In[133]:


def extract(url):
    header = {
  "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
        
  "X-Requested-With": "XMLHttpRequest"
}
    r = get_legacy_session().get(url, headers=header)
    return r
    


# In[134]:


url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"


# In[135]:


zip_file = extract(url)
z = zipfile.ZipFile(io.BytesIO(zip_file.content))
z.extract("data.csv")
df = pd.read_csv("data.csv", sep=";",on_bad_lines='skip')


# In[136]:


df.info()


# In[137]:


df2= df.iloc[:,[0,1,2,3,4,9,10]]


# In[138]:


df2.info()


# In[139]:


df2 = df2.rename(columns={'Batterietemperatur in °C': 'Batterietemperatur', 'Temperatur in °C (DWD)': 'Temperatur'})


# In[140]:


df2


# In[156]:


df3 = df2


# In[157]:


df3["Temperatur"].replace(',','.',regex=True,inplace=True)
df3["Batterietemperatur"].replace(',','.',regex=True,inplace=True)


# In[158]:


df3


# In[159]:


df3["Temperatur"] = df3["Temperatur"].astype(float)*9/5+32
df3["Batterietemperatur"] = df3["Batterietemperatur"].astype(float)*9/5+32


# In[160]:


df3


# In[162]:


(df3['Geraet'] > 0).all()



# In[163]:


df3.info()


# In[166]:


conn = sqlalchemy.create_engine('sqlite:///temperatures.sqlite')

df_data_types = {
    'Geraet': 'BIGINT',
    'Hersteller': 'TEXT ',
    'Model' :'TEXT ',
    'Monat': 'FLOAT',
    'Temperatur': 'FLOAT' ,
    'Batterietemperatur': 'FLOAT',
    'Geraet aktiv': 'TEXT ',


    
    
}


df3.to_sql('temperatures', con=conn, if_exists='replace', index=False , dtype=df_data_types)

conn.dispose()

