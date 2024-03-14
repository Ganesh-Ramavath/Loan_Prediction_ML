#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


test=pd.read_csv("test.csv")
test


# In[12]:


export_test=pd.read_csv("export_csv")
export_test


# In[13]:


export_test.describe()


# In[15]:


export_test.dtypes


# In[16]:


export_test.shape


# In[17]:


export_test.info


# In[18]:


export_test.info()


# In[19]:


export_test.columns


# In[20]:


export_columns=export_test.columns
export_columns


# In[21]:


export_test.index


# In[22]:


test.describe


# In[23]:


test.info()


# In[24]:


test.index


# In[25]:


test.columns


# In[26]:


test.describe()


# In[27]:


test.info


# In[28]:


test.info()


# In[35]:


test.index


# In[36]:


test.head()


# In[37]:


test["ApplicantIncome"].sum()


# In[38]:


test[["ApplicantIncome","LoanAmount"]].mean()


# In[39]:


test.sum()


# In[40]:


len(test)


# In[41]:


test.tail(10)


# In[42]:


test.loc[77]


# In[50]:


test.iloc[77]


# In[49]:


test.plot(kind="scatter", x="ApplicantIncome", y="Credit_History")



# In[59]:


test.plot(kind="hist", x="ApplicantIncome", y="Credit_History")


# In[61]:


export_test


# In[62]:


export_test.index


# In[63]:


export_test.plot(kind="scatter", x="ApplicantIncome",y="Credit_History")

