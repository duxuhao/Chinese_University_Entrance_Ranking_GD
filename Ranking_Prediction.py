# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVR
from sklearn.svm import SVC
from sklearn.linear_model import BayesianRidge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import itertools
from multiprocessing import Pool

pool = Pool(4)

colors = itertools.cycle(["k","r","g","b","y"])
df = pd.read_csv("UniversityData.csv") #kind of origin data
df = df[~np.isnan(df["Ranking_Scores"])] #exclude the university with no university ranking (not much)
#df = df[~np.isnan(df["Media_Impact"])]
df = df[df["Topic"] == "理科"] #select the topic
high = 50000
low = 0
df = df[df["Lowest_Ranking"] <= high] #select the regression range
df = df[df["Lowest_Ranking"] > low]
#df[np.isnan(df["Ranking_Scores"])] = 0
#df[np.isnan(df["Media_Impact"])] = 0
df = df[~np.isnan(df["GDP_Per_Person"])] #exclude some
df = df[~np.isnan(df["Distance"])] #exclude some
X =  df[["Year","UniversityNo","Ranking_Scores","Media_Impact","Distance","Plan_Number","X1A_Number","GDP_Per_Person"]]
#X =  df[["Year","UniversityNo","Ranking_Scores","Plan_Number","X1A_Number","GDP_Per_Person"]]
y = df["Ranking_Percentage"]
#y=df["Lowest_Ranking"]
#print(df.shape)

#scikit learn
names = ["Random Forest","Decision Tree","Boost Decision Tree", "Boost Random Forest"]

regression = [RandomForestRegressor(random_state=0, n_estimators=5000),
		DecisionTreeRegressor(),
		AdaBoostRegressor(DecisionTreeRegressor()),
		AdaBoostRegressor(RandomForestRegressor())]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

N = 0.1
To = np.zeros(len(df))
for name, est in zip(names[:], regression[:]):
	est.fit(X_train, y_train)
        score = est.score(X_test, y_test)
	plt.scatter(est.predict(X), y, c = next(colors),label = name)
	plt.hold("on")
	To = To + est.predict(X)
	print name + ": " + str(score)
	print "The error within " + str(N*100) + "%: " + str(100*sum((np.abs(est.predict(X)-y)/y) < N)/len(df)) + "%"
	print "The error within " + str(N*100) + "%: " + str(100*sum((np.abs(est.predict(X_test)-y_test)/y_test) < N)/len(y_test)) + "%"
'''
#pybrain
ds = SupervisedDataSet(7,1)
test = SupervisedDataSet(7,1)
for index in range(len(X_train)):
		ds.addSample(X_train[index:index+1],y_train[index:index+1])

for index in range(len(X_test)):
		test.addSample(X_test[index:index+1],y_test[index:index+1])

net = buildNetwork(7,10,10,1)
trainer = BackpropTrainer(net, ds)
trainer.train()
trainer.trainUntilConvergence(maxEpochs = 3000)
Pre_NN = np.round(net.activateOnDataset(test))
print('Neural Network: ' + str(np.corrcoef(Pre_NN.T,y_test.T)[0][1]))
'''

#plt.plot([0,50000],[0,50000])
plt.xlabel("Prediction", fontsize = 14)
plt.ylabel("Test", fontsize = 14)
plt.legend()
plt.show()

	


