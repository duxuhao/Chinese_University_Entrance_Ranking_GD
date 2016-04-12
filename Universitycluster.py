# -*- coding: utf-8 -*-
import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("UniversityData.csv")
#df = df[~np.isnan(df.Score_Last_Year)]
df['Plan_Number_Total'] = pd.Series(np.zeros(len(df)),index=df.index)
df['New_Label'] = pd.Series(np.zeros(len(df)),index=df.index)
df.Label = 0
#df = df.drop("Label",1)
df.Topic[df.Topic == "理科"] = 1
df.Topic[df.Topic == "文科"] = 0
#the comment script is for obtaining the training label

for y in range(2010,2016):
	for t in range(2):
		T = df[(df.Year == y) & (df.Topic == t)].Score
		boundary = np.max(T.values)
		a = 1
		n = 0
		Top = boundary + 50
		while a:
			try:
				boundary = boundary - (Top - boundary) * 0.01
				df.loc[(df.Year == y) & (df.Topic == t) & (df.Score < boundary),'Label']  += 1
				n += 1
				boundary = np.max(T.values[T.values < boundary])
			except:
				a = 0

trainlabel = pd.read_csv("University_data_cluster.csv")
est = AdaBoostRegressor(DecisionTreeRegressor())
colname = trainlabel.columns

df2 = df.merge(trainlabel[["UniversityNo","Topic","Year","Lowest","Last_Ranking","Average_Ranking"]],on=["UniversityNo","Topic","Year"])

df2 = df2[~np.isnan(df2.Lowest)]
df2 = df2[~(df2["Average_Ranking"] == 0)]
X = df2[["UniversityNo","Year","Topic","Lowest","Ranking_Scores","Last_Ranking","Average_Ranking"]]

y = df2.Label
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
est.fit(X_train,y_train)
print est.score(X_test,y_test)

df2.New_Label = est.predict(X)

for y in range(2011,2016):
	for t in range(2):
		s = 0
		while sum(df2.Label >= s):
			df2.loc[(df2.Year == y) & (df2.Topic == t) & (df2.Label >= s),'Plan_Number_Total'] += sum(df2.loc[(df2.Year == y) & (df2.Topic == t) & (np.round(df2.Label) ==s),'Plan_Number'])
			s += 1
			
dfsave = df2
dfsave.to_csv("University.csv")
