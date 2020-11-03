#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 15:00:23 2020

@author: JasonKhu
"""
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

os.getcwd()
os.chdir("/Users/JasonKhu/Desktop/WIT x Nine/Dataset/Data")
os.getcwd()
data = pd.read_csv("users.csv")
data.head()

graph1 = data['pages viewed per session'].plot(kind='hist',
    figsize=(14,8),
    bins = 500,
    title="pages viewed per session")

graph2 = data['bounce_int'].plot(kind='hist',
    figsize=(14,8),
    bins = 10,
    title="bounce_int")

graph3 = data['% unique sessions'].plot(kind='hist',
    figsize=(14,8),
    bins = 10,
    title="% unqiue sessions")

graph4 = data['Number of unique IP addresses'].plot(kind='hist',
    figsize=(14,8),
    bins = 140,
    title="Number of unique IP addresses")

