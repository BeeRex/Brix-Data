#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('C:/Users/Ben/Desktop/brix by density.csv', skiprows=1)
df.drop(index=0,inplace=True)
df.dtypes


# In[3]:


df['Alcohol (% v/v)'] = df['Alcohol (% v/v)'].astype("float")
df['Concentration Sugar'] = df['Concentration Sugar'].astype("float")
df.dtypes


# In[4]:


brix_data =df[['Alcohol (% v/v)','Concentration Sugar','Sample Name']]


# In[5]:


brix_data[['Alcohol (% v/v)','Concentration Sugar']].mean()


dfg = brix_data.groupby(['Sample Name'], as_index=False).mean()
dfg


# In[6]:


df2 = pd.read_csv('C:/Users/Ben/Desktop/abbemat results.csv')
df2.head()


# In[25]:


df3 = pd.merge(dfg,df2,on='Sample Name')

df3.rename(columns={'Concentration Sugar':'Density Meter Brix'},inplace=True)
df3.sort_values(by='Alcohol (% v/v)', inplace=True)


# In[24]:


plt.plot(df3['Alcohol (% v/v)'],df3['Density Meter Brix'])
plt.plot(df3['Alcohol (% v/v)'],df3['Abbemat Brix'])
plt.title('Comparing Apparent Brix: Density vs Refractive index') # add a title to the histogram
plt.ylabel('Apparent Brix') # add y-label
plt.xlabel('Alcohol (%v/v)') # add x-label
plt.show()


# In[39]:


df4 = df3
df4['Absolute Density'] = (df4['Density Meter Brix']-10)*-1
df4['Absolute Brix'] = (df4['Abbemat Brix']-10)
df4.head()


# In[42]:


plt.plot(df3['Alcohol (% v/v)'],df3['Absolute Density'])
plt.plot(df3['Alcohol (% v/v)'],df3['Absolute Brix'])
plt.title('Comparing Apparent Brix: Density vs Refractive index') # add a title to the histogram
plt.ylabel('Absolute Value of Change of Brix') # add y-label
plt.xlabel('Alcohol (%v/v)') # add x-label
plt.show()


# In[ ]:




