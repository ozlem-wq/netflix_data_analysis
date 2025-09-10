#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

def parse_date_added(df):
    """'date_added' sütununu datetime formatına çevirir"""
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    return df

def explode_listed_in(df):
    """'listed_in' sütununu explode eder (türleri ayırır)"""
    df_exploded = df.assign(
        listed_in=df['listed_in'].str.split(', ')
    ).explode('listed_in')
    return df_exploded



# In[ ]:




