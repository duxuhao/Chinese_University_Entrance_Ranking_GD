# -*- coding: utf-8 -*-
import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv("UniversityCluster.csv")
df2 = pd.read_csv("UniversityMarksFull.csv")
df2.columns = ["University_Name_Location","Year","Lowest","Highest","ave","Plan","NO","Topic"]

df2.Year += 1
'''
df2.Highest[np.isnan(df2.Highest)] = 10000
df2.ave[np.isnan(df2.ave)] = 10000
df2.Lowest[np.isnan(df2.Lowest)] = 10000
'''
df = df1.merge(df2,on=['University_Name_Location','Year','Topic'])
df.to_csv("UniversityClusterData.csv")
