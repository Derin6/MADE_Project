#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Raw URL of the Excel file in the GitHub repository
data_1_url = 'https://github.com/Derin6/MADE_Project/raw/77927c42c204107353521835a03242dcc45f1f66/project/efotw-2023-master-index-data-for-researchers-iso.xlsx'

# Read the Excel file from the raw GitHub URL into a DataFrame
df_1 = pd.read_excel(data_1_url, engine='openpyxl',sheet_name="EFW Panel Data for Researchers")

# Now, df contains the data from the Excel file



# In[3]:


df_1


# In[4]:


df_1.info()


# In[5]:


list=(2000,2003,2006,2009,2012,2015,2018)


# In[6]:


df_1 = df_1[df_1['Year'].isin(list)]



# In[7]:


df_1.dropna(inplace=True)


# In[8]:


df_1.info()


# In[9]:


url = 'https://github.com/Derin6/MADE_Project/raw/6660145197a52a4e575c31787e1c7965b62121a9/project/IDEExcelExport-Nov032023-0513PM.xls'
firs_dt=pd.read_excel(url,skiprows=11,nrows=285-12,usecols="B:E",engine="xlrd" )


# In[10]:


firs_dt


# In[11]:


counter=0

for i in range(273):
    if pd.isnull(firs_dt["Year/Study"][i]) == False :
        year = float(firs_dt["Year/Study"][i])
    else:
        firs_dt["Year/Study"][i] = year
        float(firs_dt["Year/Study"][i])
        
        counter=+1
print(counter)


# In[12]:


firs_dt.info()


# In[13]:


countries=firs_dt['Jurisdiction'].unique()


# In[14]:


import numpy as np
countries=countries.tolist()
del countries[0:2]


# In[15]:


countries


# In[16]:


df_1 = df_1[df_1['Countries'].isin(countries)]
df_1 = df_1[df_1['Year'].isin(list)]


# In[17]:


df_1


# In[18]:


countries_2=df_1['Countries'].unique()


# In[19]:


countries_2=countries_2.tolist()
del countries_2[0:1]


# In[20]:


countries_2


# In[21]:


firs_dt = firs_dt[firs_dt['Jurisdiction'].isin(countries_2)]


# In[22]:


firs_dt


# In[23]:


df_1


# In[24]:


# Print column names of df_1 and firs_dt
print("Columns in df_1:", df_1.columns)
print("Columns in firs_dt:", firs_dt.columns)


# In[25]:


firs_dt=firs_dt.rename(columns={"Jurisdiction":"Countries"})
firs_dt=firs_dt.rename(columns={"Year/Study":"Year"})


# In[26]:


columns = ["Year", "Countries"]

# Assuming df_1 and firs_dt are your DataFrames
df3 = df_1.merge(firs_dt[columns], on=columns, how="inner")
df4 = firs_dt.merge(df_1[columns], on=columns, how="inner")


# In[27]:


df3


# In[28]:


df4


# In[31]:


from sqlalchemy import create_engine
import pandas as pd

# Step 1: Create a SQLAlchemy Engine with a new SQLite database
db_url = 'sqlite:///made_database.db'
engine = create_engine(db_url)





# In[34]:


# Step 3: Insert DataFrame into the Database
table_2 = 'table_2'
df4.to_sql(table_2, con=engine, if_exists='replace')


# In[33]:


query = f'SELECT * FROM {table_1}'
result = pd.read_sql_query(query, con=engine)
print(result)


# In[35]:


query = f'SELECT * FROM {table_2}'
result = pd.read_sql_query(query, con=engine)
print(result)


# In[ ]:




