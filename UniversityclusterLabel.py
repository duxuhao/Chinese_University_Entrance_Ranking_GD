# -*- coding: utf-8 -*-
import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv("UniversityData.csv")
df1['Average_Ranking'] = pd.Series(np.zeros(len(df1)),index=df1.index)
df1['Last_Ranking'] = pd.Series(np.zeros(len(df1)),index=df1.index)
df1.Topic[df1.Topic == "理科"] = 1
df1.Topic[df1.Topic == "文科"] = 0
UniNoList = df1.UniversityNo.unique()
for No in UniNoList:
	for Y in range(2011,2016):
		for t in range(2):
			ave = np.mean(df1[(df1.Topic == t) &( df1.UniversityNo == No) & (df1.Year < Y)].Lowest_Ranking)
			df1.loc[(df1.Topic == t) &( df1.UniversityNo == No) & (df1.Year == Y),'Average_Ranking'] = ave
			last = df1[(df1.Topic == t) &( df1.UniversityNo == No) & (df1.Year == Y-1)].Lowest_Ranking
			try:
				df1.loc[(df1.Topic == t) &( df1.UniversityNo == No) & (df1.Year == Y),'Last_Ranking'] = last.values
			except:
				pass

df2 = pd.read_csv("UniversityMarksFull.csv")
df2.columns = ["University_Name_Location","Year","Lowest","Highest","ave","Plan","NO","Topic"]

df2.Year += 1

df2.Lowest[np.isnan(df2.Lowest)] = df2.Lowest[np.isnan(df2.ave)]
df2.Lowest[np.isnan(df2.Lowest)] = df2.Lowest[np.isnan(df2.Highest)]

df2.Topic[df2.Topic == "理科"] = 1
df2.Topic[df2.Topic == "文科"] = 0
df = df1.merge(df2[["University_Name_Location","Year","Lowest","Topic"]],on=['University_Name_Location','Year','Topic'])

selected_column = ["UniversityNo",'Year','Topic',"Lowest","GDP","Population","GDP_Per_Person","Plan_Number","Ranking_Scores","Media_Impact","Distance","Last_Ranking","Average_Ranking"]
df = df[selected_column]
df = df[~np.isnan(df.Last_Ranking)]
df = df[~np.isnan(df.Average_Ranking)]
df.to_csv("University_data_cluster.csv")
