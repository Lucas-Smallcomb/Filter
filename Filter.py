#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import os

# Creates a dataframe from a .csv file
file_path = "C:/Users/nobody/Documents/Microsoft Malware Prediction Datasets/train.csv"
data = pd.read_csv(file_path)


# In[4]:


# Removes a column "Census_IsPenCapable" if run
data.drop("Census_IsPenCapable", axis = 1, inplace = True)


# In[5]:


# Shows full dataframe (truncated)
data


# In[7]:


import numpy

# Describes the dataframe filtering for numeric types
data.describe(include = numpy.number)


# In[8]:


# Describes the dataframe filtering for objects
data.describe(include = numpy.object)

