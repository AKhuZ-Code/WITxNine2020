import os
# import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import sqlite3
from datetime import datetime
pd.set_option('display.max_columns', None)


# read files and create data frame

os.getcwd()
os.chdir("/Users/JasonKhu/Desktop/WIT x Nine/Dataset/Data")
os.getcwd()

data = pd.DataFrame()
file_list = glob.glob('/Users/JasonKhu/Desktop/WIT x Nine/Dataset/Data/*')

dfs = []
for file in file_list:
    data = pd.read_csv(file, quotechar='"')
    print(file + '  ---> ' + str(len(data.index)))
    # print(data.loc[0,:]) # print a record
    dfs.append(data)
    #break

# concatenate all data frames as one
data = pd.concat(dfs, ignore_index=True) 

# correct is 3,659,406
print(str(len(data.index)))

# query data using pandas -to get a feel of the dataset
print(data.groupby('domain_userid').size().head())
print(data.groupby('member_type').size().head()) #2618810 non subscribers
print(data.groupby('os_family').size()) #Alot of traffic from windows
print(data.groupby('os_name').size())

#following code is for EDA - involving bar charts
plot_articletype = dataset2['article_type'].value_counts().plot(kind='bar',
    figsize=(14,8),
    title="Article_type sessioned")
plot_osfamilyused = dataset2['os_family'].value_counts().plot(kind='bar',
    figsize=(14,8),
    title="OS Family used")
plot_osnameused = dataset2['os_name'].value_counts().plot(kind='bar',
    figsize=(14,8),
    title="OS Name used")
plot_brfamused = dataset2['br_family'].value_counts().plot(kind='bar',
    figsize=(14,8),
    title="Browser family used")
plot_brtypeused = dataset2['br_type'].value_counts().plot(kind='bar',
    figsize=(14,8),
    title="Browser type used")
plot_membertype = dataset2['member_type'].value_counts().plot(kind='bar',
    figsize=(14,8),
    title="member_type sessioned")
plot_pgurlscheme = dataset2['page_urlscheme'].value_counts().plot(kind='bar',
    figsize=(14,8),
    title="page_urlscheme")
plot_referurlscheme = dataset2['refr_urlscheme'].value_counts().plot(kind='bar',
    figsize=(14,8),
    title="refr_urlscheme")
plot_pageurlport = dataset2['page_urlport'].value_counts().plot(kind='bar',
    figsize=(14,8),
    title="page_urlport")
plot_articleprimarycategory = dataset2['article_primary_category'].value_counts().head(10).plot(kind='bar',
    figsize=(14,8),
    title="article_primary_category")
plot_referurlhost = dataset2['refr_urlhost'].value_counts().head(20).plot(kind='bar',
    figsize=(14,8),
    title="refr_urlhost")
