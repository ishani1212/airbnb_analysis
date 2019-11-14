#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


# In[2]:


import scipy
import seaborn as sns


# In[5]:



airbnb = pd.read_csv("AB_NYC_2019.csv")
airbnb.describe()


# In[6]:


airbnb.info()


# In[7]:


airbnb.head()


# In[8]:


#drop columns "host_id" and "host_name" as there is no need of them in data analysis
airbnb.drop(["host_id","host_name","last_review"], axis=1, inplace=True)


# In[9]:


#showing missing value 
airbnb.isnull().sum()


# In[10]:


#in review per month fill missing value with "0"
airbnb['reviews_per_month']= airbnb["reviews_per_month"].fillna(0)


# In[11]:


#missing value in name will change by "no comment"
airbnb['name']=airbnb["name"].fillna("no commnet")


# In[12]:


#check for missing value again
airbnb.isnull().sum()


# In[13]:


#find unique values in neighbourhood_group
airbnb['neighbourhood_group'].unique()


# In[14]:


#find unique values in neighbourhood
airbnb['neighbourhood'].unique()


# In[15]:


#find room_type unique
airbnb['room_type'].unique()


# ##                                       let's start with EDA
# 

# In[16]:


plt.figure(figsize=(16,8))
sns.countplot(x='room_type',data=airbnb)
plt.show()

#according to chart most choose room type is entire home 


# In[17]:


plt.figure(figsize=(16,8))
sns.countplot(x="neighbourhood_group", hue="room_type", data=airbnb)
plt.show()

# it seems that Manhattan has highest entire home/apt among other neighbourhood groups
# perhaps majority of guests go to Manhattan are either group of friends or family members
# shared room has very significant low number among all neighbourhood groups
# possibly couples would not choose those neighbourhood groups as their vacation spots


# In[20]:


df_price = airbnb.groupby("neighbourhood_group").agg({"price":"mean"}).sort_values("price", ascending=False).reset_index()
plt.figure(figsize=(16,8))
sns.barplot(x="neighbourhood_group", y="price", data=df_price)
plt.show()

# it seems Manhattan charges highest average price among other neighbourhood groups
# perhaps Manhattan is the most popular vacation spot
# this is also due to Manhattan has the highest number of entire home/apt among other neighbourhood groups
# entire home/apt will charge higher price than private and shared rooms


# In[30]:


df_night = airbnb.groupby("neighbourhood_group").agg({"minimum_nights":"mean"}).sort_values("minimum_nights", ascending=False).reset_index()

plt.figure(figsize=(16,8))
sns.barplot(x="neighbourhood_group", y="minimum_nights", data=df_night)
plt.show()
# it seems most of guests would like to stay at Manhattan longer than other neighbourhood groups


# In[31]:


df_review = airbnb.groupby("neighbourhood_group").agg({"number_of_reviews":"sum"}).sort_values("number_of_reviews", ascending=False).reset_index()

plt.figure(figsize=(16,8))
sns.barplot(x="neighbourhood_group", y="number_of_reviews", data=df_review)
plt.show()
# it seems that Brooklyn has the highest sum of number of reviews among other neighbourhood groups
# but we cannot tell from here whether those reviews are good or bad
# what we can tell from here is guests are defenitely love to review about Brooklyn accomodations


# In[32]:


df_neighbourhood = airbnb["neighbourhood"].value_counts().head(10).reset_index()
df_neighbourhood.columns = ["neighbourhood","counts"]

plt.figure(figsize=(16,8))
sns.barplot(x="neighbourhood", y="counts", data=df_neighbourhood)
plt.show()
# it seems Williamsburg is the most popular choice for guests to stay overnight
# Williamsburg is a hip neighborhood in Brooklyn and it is one of the popular vacation spot.


# In[35]:


df_availablity = airbnb.groupby("neighbourhood_group").agg({"availability_365":"mean"}).sort_values("availability_365", ascending=False).reset_index()

plt.figure(figsize=(16,8))
sns.barplot(x="neighbourhood_group", y="availability_365", data=df_availablity)
plt.show()

#staten island has most availablity and brooklyn has less availablity.


# In[37]:


import folium
from folium.plugins import HeatMap

airbnb_map = folium.Map(location = [40.71,-74.01], zoom_start=11)
HeatMap(airbnb[["latitude","longitude"]],radius=8, gradient={0.4:"blue",0.65:"purple",1.0:"red"}).add_to(airbnb_map)
airbnb_map
# it seems like center of New York is highly populated.


# In[ ]:




