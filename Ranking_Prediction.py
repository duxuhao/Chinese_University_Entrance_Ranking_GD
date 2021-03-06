# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
'''
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
'''
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM
import itertools
from multiprocessing import Pool
from sklearn.decomposition import PCA
import plotly.plotly as py
import plotly.graph_objs as go
import ggplot
import seaborn as sns

pool = Pool(4)

colors = itertools.cycle(["k","g","r","b","y"])
df = pd.read_csv("Produce_Data/University.csv") #kind of origin data
df = df[~np.isnan(df["Ranking_Scores"])] #exclude the university with no 
#df = df[df["Topic"] == 1] #select the topic

high = 50000
low = 0
'''
df = df[df["Lowest_Ranking"] <= high] #select the regression range
df = df[df["Lowest_Ranking"] > low]
'''
df = df[~np.isnan(df["GDP_Per_Person"])] #exclude some
df = df[~np.isnan(df["Distance"])] #exclude some

fea = ["UniversityNo","Average_Ranking","Last_Ranking","Distance","GDP_Per_Person","Ranking_Scores","Media_Impact","Year","Topic","Plan_Number","Plan_Number_Total"]
New =  df[fea[:]]
'''
pca = PCA(n_components = 4)
X = pca.fit_transform(New)
'''
X=New
print "Features include:"
print ','.join(map(str,X.columns))
y=df.Lowest_Ranking

#scikit learn
names = ["Random Forest","Decision Tree"]

regression = [RandomForestRegressor(random_state=0, n_estimators=5000),
		AdaBoostRegressor(DecisionTreeRegressor())]

X_train1, X_test1, y_train, y_test = train_test_split(X, y, test_size = 0.3)
X_train = X_train1[fea[3:]]
X_test = X_test1[fea[3:]]

N = 0.05
To = np.zeros(len(df))
Y_combine = np.zeros(len(y_test))
n = 0
Top = 2000
bound = 0.15

for name, est in zip(names[1:], regression[1:]):
	est.fit(X_train, y_train)
        score = est.score(X_test, y_test)
	pre = est.predict(X_test)
	Ave = (pre - X_test1.Last_Ranking.values)
	adjust = np.abs(Ave/X_test1.Last_Ranking).values
	Use = (adjust >= bound) & (X_test1.Last_Ranking.values < Top )
	print "----------------"
	print name + ": " + str(round(1000*score)/10) + "%"
	print "----------------"
	print "The error within " + str(N*200) + "%: " + str(round(1000*sum((np.abs(pre-y_test)/y_test) < N*2)/len(y_test))/10) + "%"
	print "The error within " + str(N*100) + "%: " + str(round(1000*sum((np.abs(pre-y_test)/y_test) < N)/len(y_test))/10) + "%"
	print "The mean error: " + str(round(1000 * np.mean(np.abs(pre-y_test)/y_test))/10) + "%"
	print "----------------"
	with sns.axes_style('darkgrid'):
		plt.subplot(211)
		plt.bar(range(len(fea[3:])),est.feature_importances_)
		plt.xticks(np.arange(len(fea[3:]))+0.5,fea[3:],fontsize=12)
		plt.ylabel('Importance',fontsize=14)
		plt.subplot(212)
		plt.scatter(pre,y_test,c = 'r', label = name)
		plt.hold("on")
		plt.plot([low,high],[low*0.9,high*0.9],'--',[low,high], [low*1.1,high*1.1], '--', c = 'k', linewidth = 2)
		plt.ylabel('Real Ranking',fontsize=14)
		plt.xlabel('Prediction Ranking',fontsize=14)
	Y_combine += pre
	n += 1
	print "Top university adjust"
	pre[Use] = X_test1.Last_Ranking[Use].values # if the top university prediction is to far away from the average one, put it to the last ranking
	print "The error within " + str(N*200) + "%: " + str(round(1000*sum((np.abs(pre-y_test)/y_test) < N*2)/len(y_test))/10) + "%"
	print "The error within " + str(N*100) + "%: " + str(round(1000*sum((np.abs(pre-y_test)/y_test) < N)/len(y_test))/10) + "%"
	print "The mean error: " + str(round(1000 * np.mean(np.abs(pre-y_test)/y_test))/10) + "%"
	print "----------------"

plt.legend()
plt.xlim((0,50000))
plt.ylim((0,50000))
plt.show()


'''
	trace0 = go.Scatter(x = est.predict(X_test), y = y_test, mode = 'markers',name = 'Test')
	trace1 = go.Scatter(x = est.predict(X_train), y = y_train, mode = 'markers',name = 'Train')
	trace2 = go.Scatter(x = [low,high],y = [low*0.9,high*0.9],mode = 'lines',name = '10%' )
	trace3 = go.Scatter(x = [low,high],y = [low*1.1,high*1.1],mode = 'lines',name = '10%' )
	trace4 = go.Scatter(x = [low,high],y = [low*0.95,high*0.95],mode = 'lines',name = '5%' )
	trace5 = go.Scatter(x = [low,high],y = [low*1.05,high*1.05],mode = 'lines',name = '5%' )
	data = [trace0, trace1, trace2, trace3, trace4, trace5 ]
	layout = go.Layout(xaxis=dict(title='Prediction',ticklen=5,zeroline=False),yaxis=dict(title='Value',ticklen=5))
	fig = go.Figure(data=data,layout=layout)
	py.iplot(fig, filename='scatter-mode')
'''
'''
#keras CNN learning
hidden_neurons = 100
in_neurons = X_train.shape[1]
out_neurons = 1
method = 'relu'
model = Sequential()
model.add(Dense(hidden_neurons,input_dim=in_neurons,activation=method))
model.add(Dense(hidden_neurons,activation=method))
model.add(Dense(hidden_neurons,activation=method))
model.add(Dense(hidden_neurons,activation=method))
model.add(Dense(out_neurons))
model.compile(loss="mean_absolute_percentage_error",optimizer='RMSprop') # mean_absolute_percentage_error/mean_squared_logarithmic_error/mean_squared_error
model.fit(X_train.values, y_train.values, batch_size=450, nb_epoch=20000,validation_split=0.05)
pre = model.predict(X_test.values).T

print "CNN:"
print "The error within " + str(N*200) + "%: " + str(100*sum((np.abs(pre-y_test.values)/y_test.values)[0] < N*2)/len(y_test.values)) + "%"
print "The error within " + str(N*100) + "%: " + str(100*sum((np.abs(pre-y_test.values)/y_test.values)[0] < N)/len(y_test.values)) + "%"
'''
