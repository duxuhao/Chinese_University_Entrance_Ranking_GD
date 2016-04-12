# -*- coding: utf-8 -*-

#combine the university score of different year to the original dataset
import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv("Produce_Data/UniversityData.csv")
df1['Average_Ranking'] = pd.Series(np.zeros(len(df1)),index=df1.index)
df1['Last_Ranking'] = pd.Series(np.zeros(len(df1)),index=df1.index)
df1.Topic[df1.Topic == "理科"] = 1
df1.Topic[df1.Topic == "文科"] = 0
UniNoList = df1.UniversityNo.unique() #obtain the university number

# obtain the average ranking in previous year and the last year
for No in UniNoList: # loop university number
	for Y in range(2011,2016): # loop year
		for t in range(2): #loop topic
			ave = np.mean(df1[(df1.Topic == t) &( df1.UniversityNo == No) & (df1.Year < Y)].Lowest_Ranking)
			df1.loc[(df1.Topic == t) &( df1.UniversityNo == No) & (df1.Year == Y),'Average_Ranking'] = ave
			last = df1[(df1.Topic == t) &( df1.UniversityNo == No) & (df1.Year == Y-1)].Lowest_Ranking
			try:
				df1.loc[(df1.Topic == t) &( df1.UniversityNo == No) & (df1.Year == Y),'Last_Ranking'] = last.values
			except:
				pass

df2 = pd.read_csv("Original_Data/UniversityMarksFull.csv") #the score of different years of universities
df2.columns = ["University_Name_Location","Year","Lowest","Highest","ave","Plan","NO","Topic"]

df2.Year += 1 #set to predict the next year
# in some university, no lowest score data provided, so we use the ave andhighest to present
df2.Lowest[np.isnan(df2.Lowest)] = df2.Lowest[np.isnan(df2.ave)]
df2.Lowest[np.isnan(df2.Lowest)] = df2.Lowest[np.isnan(df2.Highest)]

df2.Topic[df2.Topic == "理科"] = 1
df2.Topic[df2.Topic == "文科"] = 0

df = df1.merge(df2[["University_Name_Location","Year","Lowest","Topic"]],on=['University_Name_Location','Year','Topic']) #merge some content of df2 to df1 
#select some columns to produce the useful data
selected_column = ["UniversityNo",'Year','Topic',"Lowest","GDP","Population","GDP_Per_Person","Plan_Number","Ranking_Scores","Media_Impact","Distance","Last_Ranking","Average_Ranking"]
df = df[selected_column]
df = df[~np.isnan(df.Last_Ranking)]
df = df[~np.isnan(df.Average_Ranking)]
df = df[~(df.Average_Ranking == 0)] #average ranking in 2010 is zero 
df.to_csv("Produce_Data/University_data_cluster.csv") #the data pass for label training
