#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os

file_path = "C:/Users/nobody/Documents/Microsoft Malware Prediction Datasets/train.csv"
data = pd.read_csv(file_path)

print(type(data))


# In[7]:


data.drop("Census_IsPenCapable", axis = 1, inplace = True)


# In[8]:


data

