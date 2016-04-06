import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer


df = pd.read_csv("No_chinese_feature.csv")
#df = df[~np.isnan(df["Ranking_Scores"])]
#df = df[~np.isnan(df["Media_Impact"])]
df[np.isnan(df["Ranking_Scores"])] = 0
df[np.isnan(df["Media_Impact"])] = 0
X =  df[["Year","Ranking_Scores","Media_Impact","Plan_Number","X1A_Number","GDP_Per_Person"]]
y = df["Level"]

print(df.shape)

#scikit learn
names = ["Nearest Neighbors", "RBF SVM", "Decision Tree",
         "Random Forest", "AdaBoost"]

classifiers = [
	KNeighborsClassifier(20),
	SVC(gamma=10, C=1),
	DecisionTreeClassifier(),
	RandomForestClassifier(),
	AdaBoostClassifier(),]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

for name, clf in zip(names, classifiers):
	clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)
	print name + ": " + str(score)

#pybrain
ds = SupervisedDataSet(6,1)
test = SupervisedDataSet(6,1)
for index in range(len(X_train)):
		ds.addSample(X_train[index:index+1],y_train[index:index+1])

for index in range(len(X_test)):
		test.addSample(X_test[index:index+1],y_test[index:index+1])

net = buildNetwork(6,10,10,1)
trainer = BackpropTrainer(net, ds)
trainer.train()
trainer.trainUntilConvergence(maxEpochs = 3000)
Pre_NN = np.round(net.activateOnDataset(test))
print('Neural Network: ' + str(np.corrcoef(Pre_NN.T,y_test.T)[0][1]))


	


