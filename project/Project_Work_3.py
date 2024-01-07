#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3
import urllib.request
from pandas.testing import assert_frame_Qequal
import example
import requests
from sqlalchemy import create_engine
from io import BytesIO
import ssl
import urllib3




# In[2]:


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


# In[3]:


def extract(url):
    header = {
  "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
        
  "X-Requested-With": "XMLHttpRequest"
}
    r = get_legacy_session().get(url, headers=header)
    return r
    


# In[4]:


def read_excel_1(r):
    content = r.content
    df1=pd.read_excel(BytesIO(content), engine="openpyxl",skiprows=4,nrows=203-4)
    return df1


def read_excel_2(r):
    content = r.content
    df2=pd.read_excel(BytesIO(content), engine="openpyxl",skiprows=2)
    return df2

    


# In[93]:


def transform(df1,df2):
    df1.drop(df1.columns[[0,3,5,7,9,11,12,13]], axis=1, inplace=True)
    df1=df1.rename(columns={"Unnamed: 1":"Country"})
    df2=df2.loc[df2['Unit of measurement'] == "Rate per 100,000 population"]
    df2=df2.loc[df2['Sex'] == "Total"]
    df2=df2.loc[df2['Year'] == 2021]
    df2.dropna()
    columns = [ "Country"]

    df1 = df1.merge(df2[columns], on=columns, how="inner")
    df2 = df2.merge(df1[columns], on=columns, how="inner")
    
    df1.drop_duplicates(inplace=True)
    df1.reset_index(inplace=True)
    df1.drop(["index","HDI rank"], axis=1, inplace=True)
    df1['Human Development Index (HDI) '] = df1['Human Development Index (HDI) '].astype(float)
    df1['Life expectancy at birth'] = df1['Life expectancy at birth'].astype(float)
    df1['Expected years of schooling'] = df1['Expected years of schooling'].astype(float)
    df1['Mean years of schooling'] = df1['Mean years of schooling'].astype(float)
    df1['Gross national income (GNI) per capita'] = df1['Gross national income (GNI) per capita'].astype(float)




    
    df2.drop_duplicates(inplace=True)
    df2.reset_index(inplace=True)
    df2.drop(df2.columns[[0,1,3,4,6,8,9,13]], axis=1, inplace=True)
    df2 = df2.groupby(['Country', 'Indicator'])['VALUE'].sum().reset_index()
    
    columns = [ "Country"]

    df1 = df1.merge(df2[columns], on=columns, how="inner")
    df2 = df2.merge(df1[columns], on=columns, how="inner")
    
    df1.drop_duplicates(ignore_index=True,inplace=True)
    df2.drop_duplicates(ignore_index=True,inplace=True)
    
    df3=df2[df2['Indicator'] == "Acts against the environment"]
    df4=df2[df2['Indicator'] == "Offences"]
    
    df3.reset_index(drop=True,inplace=True)
    df4.reset_index(drop=True,inplace=True)
    
    df5 = pd.merge(df1, df3, on='Country', how='inner')
    df6 = pd.merge(df1, df4, on='Country', how='inner')




    
    return df5 , df6


    


    

    

    


# In[94]:


url1="https://hdr.undp.org/sites/default/files/2021-22_HDR/HDR21-22_Statistical_Annex_HDI_Table.xlsx"
url2="https://dataunodc.un.org/sites/dataunodc.un.org/files/data_cts_corruption_and_economic_crime.xlsx"


# In[95]:


r1 = extract(url1)
r2 = extract(url2)


# In[96]:


df1 = read_excel_1(r1)
df2 = read_excel_2(r2)


# In[97]:


df1,df2 = transform(df1,df2)




# In[103]:


conn = sqlite3.connect('git.sqlite')
cursor = conn.cursor()

df_data_types = {
    'Country': 'BLOB',
    'Human Development Index (HDI)': 'BLOB',
    'Life expectancy at birth' :'BLOB',
    'Expected years of schooling': 'BLOB',
    'Mean years of schooling': 'BLOB' ,
    'Gross national income (GNI) per capita': 'BLOB',
    'Indicator': 'BLOB',
    'VALUE': 'BLOB'


    
    
}


df1.to_sql('table_1', conn, if_exists='replace', index=False , dtype=df_data_types)
df2.to_sql('table_2', conn, if_exists='replace', index=False , dtype=df_data_types)


conn.commit()
conn.close()








