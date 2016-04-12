# -*- coding: utf-8 -*-
# traing the label to obtain the total plan number
import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("Produce_Data/UniversityData.csv")
df['Plan_Number_Total'] = pd.Series(np.zeros(len(df)),index=df.index) #the most important factor
df['New_Label'] = pd.Series(np.zeros(len(df)),index=df.index)
df['Label'] = pd.Series(np.zeros(len(df)),index=df.index)

df.Topic[df.Topic == "理科"] = 1
df.Topic[df.Topic == "文科"] = 0

#the comment script is for obtaining the training label, the label is corresponding the the exact year, which is unable to obtain in this year, but can use for label training
for y in range(2010,2016): #loop year
	for t in range(2): #loop topic
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

trainlabel = pd.read_csv("Produce_Data/University_data_cluster.csv")
#use different regression methods
est = AdaBoostRegressor(DecisionTreeRegressor())

col_predic = ["UniversityNo","Topic","Year","Lowest","Last_Ranking","Average_Ranking"] # parameter use for label training
df2 = df.merge(trainlabel[col_predic],on=["UniversityNo","Topic","Year"])

df2 = df2[~np.isnan(df2.Lowest)]
df2 = df2[~(df2["Average_Ranking"] == 0)]
X = df2[["UniversityNo","Year","Topic","Lowest","Ranking_Scores","Last_Ranking","Average_Ranking"]] #The train parameters label

y = df2.Label
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
est.fit(X_train,y_train)
print "----------------"
print "Prediction score: " + str(round(est.score(X_test,y_test)*1000)/10) + "%"
print "----------------"

df2.New_Label = est.predict(X) #obtain the prediction label for future ranking prediction
#sum up the enroll student number equal to smaller than the label, the predicting ranking numbers are mainly base on this parameter

for y in range(2011,2016): #no 2010 because no average ranking in it
	for t in range(2):
		s = 0
		while sum(df2.Label >= s):
			df2.loc[(df2.Year == y) & (df2.Topic == t) & (df2.Label >= s),'Plan_Number_Total'] += sum(df2.loc[(df2.Year == y) & (df2.Topic == t) & (np.round(df2.Label) ==s),'Plan_Number'])
			s += 1
			
dfsave = df2
dfsave.to_csv("Produce_Data/University.csv")
