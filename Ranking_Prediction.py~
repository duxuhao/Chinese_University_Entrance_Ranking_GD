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
from sklearn.decomposition import PCA

pool = Pool(4)

colors = itertools.cycle(["k","r","g","b","y"])
df = pd.read_csv("University.csv") #kind of origin data
df = df[~np.isnan(df["Ranking_Scores"])] #exclude the university with no 
#df = df[df["Topic"] == 0] #select the topic

high = 50000
low = 0
df = df[df["Lowest_Ranking"] <= high] #select the regression range
df = df[df["Lowest_Ranking"] > low]

df = df[~np.isnan(df["GDP_Per_Person"])] #exclude some
df = df[~np.isnan(df["Distance"])] #exclude some
fea = ["Year","Topic","UniversityNo","Ranking_Scores","Media_Impact","Distance","Plan_Number","GDP_Per_Person","Plan_Number_Total"]
X =  df[fea]
y=df["Lowest_Ranking"]

#scikit learn
names = ["Random Forest","Boost Random Forest"]

regression = [RandomForestRegressor(random_state=0, n_estimators=5000),
		AdaBoostRegressor(RandomForestRegressor())]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

N = 0.05
To = np.zeros(len(df))
for name, est in zip(names[:1], regression[:1]):
	est.fit(X_train, y_train)
        score = est.score(X_test, y_test)
	To = To + est.predict(X)
	print name + ": " + str(score)
	print "The error within " + str(N*200) + "%: " + str(100*sum((np.abs(est.predict(X_test)-y_test)/y_test) < N*2)/len(y_test)) + "%"
	print "The error within " + str(N*100) + "%: " + str(100*sum((np.abs(est.predict(X_test)-y_test)/y_test) < N)/len(y_test)) + "%"
	print np.mean((est.predict(X_test)-y_test)/y_test)
	plt.bar(range(len(fea)),est.feature_importances_)
	plt.xticks(range(len(fea)),fea)


plt.show()
plt.scatter(est.predict(X_test), y_test, c = next(colors),label = name)
plt.hold("on")
plt.plot([low,high],[low,high])
plt.plot([low,high*0.9],[low,high*0.9],c = 'r')
plt.plot([low,high*1.1],[low,high*1.1],c = 'r')
plt.plot([low,high*0.95],[low,high*0.95],c = 'g')
plt.plot([low,high*1.15],[low,high*1.15],c = 'g')
plt.xlabel("Prediction", fontsize = 14)
plt.ylabel("Test", fontsize = 14)
plt.legend()
plt.show()


