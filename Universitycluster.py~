# -*- coding: utf-8 -*-
import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("UniversityDataTemp2.csv")
#df = df[~np.isnan(df.Score_Last_Year)]
df['Plan_Number_Total'] = pd.Series(np.zeros(len(df)),index=df.index)
df['Previous_Rank'] = pd.Series(np.zeros(len(df)),index=df.index)
df.Label = 0

for y in range(2010,2016):
	for t in ["理科","文科"]:
		T = df[(df.Year == y) & (df.Topic == t)].Score_Last_Year
		boundary = np.max(T.values)
		a = 1
		n = 0
		Top = boundary + 50
		while a:
			try:
				boundary = boundary - (Top - boundary) * 0.07
				df.loc[(df.Year == y) & (df.Topic == t) & (df.Score_Last_Year < boundary),'Label']  += 1
				n += 1
				boundary = np.max(T.values[T.values < boundary])
			except:
				a = 0
		for s in range(n):
			df.loc[(df.Year == y) & (df.Topic == t) & (df.Label >= s),'Plan_Number_Total'] += sum(df.loc[(df.Year == y) & (df.Topic == t) & (df.Label ==s),'Plan_Number'])
dd = df[["Year","Lowest_Ranking","Topic","University_Name_Location"]]
'''
dd.loc[:,'Year'] += 1
dd.columns = ["Year","Last_Lowest_Ranking","Topic","University_Name_Location"]
df = df.merge(dd,on=["Year","Topic","University_Name_Location"])
'''
col = ["UniversityNo","University_Name","University_Name_Pinyin","University_Name_Location","Distance","Province","GDP","Population","GDP_Per_Person","Year","Student_Population","X1A_Number","Ranking_Scores","Media_Impact","Topic","Plan_Number","Plan_Number_Total","Lowest_Ranking","Label","Ranking_Percentage","Score_Last_Year"]
dfsave = df[col]
dfsave.to_csv("University.csv")
