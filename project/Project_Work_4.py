#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import sqlite3
import urllib.request
import requests
from io import BytesIO
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


# In[46]:


from pandas.testing import assert_frame_equal
import example


# In[52]:


def extract(url):
    header = {
  "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
        
  "X-Requested-With": "XMLHttpRequest"
}
    r = requests.get(url, headers=header,verify=False)
    return r
    


# In[53]:


def read_excel_1(r):
    content = r.content
    df1=pd.read_excel(BytesIO(content), engine="openpyxl",skiprows=4,nrows=203-4)
    return df1


def read_excel_2(r):
    content = r.content
    df2=pd.read_excel(BytesIO(content), engine="openpyxl",skiprows=2)
    return df2

    


# In[54]:


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


    


    

    

    


# In[55]:


url1="https://hdr.undp.org/sites/default/files/2021-22_HDR/HDR21-22_Statistical_Annex_HDI_Table.xlsx"
url2="https://dataunodc.un.org/sites/dataunodc.un.org/files/data_cts_corruption_and_economic_crime.xlsx"

r1 = extract(url1)
r2 = extract(url2)
df1 = read_excel_1(r1)
df2 = read_excel_2(r2)
df1,df2 = transform(df1,df2)


# In[56]:


def test_load():
    conn = sqlite3.connect('made_database.sqlite')
    result1 = pd.read_sql_query("SELECT * FROM table1" , conn)
    result2 = pd.read_sql_query("SELECT * FROM table2" , conn)

    conn.close()
    
    
    return assert_frame_equal(result1, df1) , assert_frame_equal(result2, df2)

    
    
    
    


# In[57]:


test_load()


# In[ ]:





# In[ ]:




