#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import sqlite3
import urllib.request
from pandas.testing import assert_frame_equal
import example
import requests
from sqlalchemy import create_engine
from io import BytesIO
import ssl




# In[3]:

ssl._create_default_https_context = ssl._create_unverified_context

def extract(url):
    header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}
    r = requests.get(url, headers=header)
    return r
    


# In[4]:


def read_excel_1(r):
    content = r.content
    df1=pd.read_excel(BytesIO(content), engine="openpyxl",skiprows=4,nrows=203-4)
    return df1

def read_excel_2(url2):
    df2=pd.read_excel(url2, engine="openpyxl",skiprows=2)
    return df2


    


# In[5]:


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
    
    return df1 , df2


    


    

    

    


# In[6]:


url1="https://hdr.undp.org/sites/default/files/2021-22_HDR/HDR21-22_Statistical_Annex_HDI_Table.xlsx"
url2="https://dataunodc.un.org/sites/dataunodc.un.org/files/data_cts_corruption_and_economic_crime.xlsx"


# In[7]:


r1 = extract(url1)


# In[8]:


df1 = read_excel_1(r1)
df2 = read_excel_2(url2)


# In[9]:


df1,df2 = transform(df1,df2)


# In[10]:


conn = sqlite3.connect('made_database.sqlite')
cursor = conn.cursor()

df1_data_types = {
    'Country': 'BLOB',
    'Human Development Index (HDI)': 'BLOB',
    'Expected years of schooling': 'BLOB',
    'Mean years of schooling': 'BLOB' ,
    'Gross national income (GNI) per capita': 'BLOB'
    
    
}


df1.to_sql('table1', conn, if_exists='replace', index=False , dtype=df1_data_types)
df2.to_sql('table2', conn, if_exists='replace', index=False)


conn.commit()


# In[11]:


conn = sqlite3.connect('made_database.sqlite')
cursor = conn.cursor()
table1="table1"

query = f'SELECT * FROM {table1}'
result = pd.read_sql_query(query, conn)
print(result)
conn.close()


# In[ ]:




