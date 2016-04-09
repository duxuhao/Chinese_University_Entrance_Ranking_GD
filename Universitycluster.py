import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("UniversityData.csv") #kind of origin data
#df = df.sort(['Score'],ascending = 0)
df.Label = 0
T = df[(df.Year == 2015) & (df.Topic == "理科")].Score
boundary = np.max(T.values)
boundary = boundary - (750 - bounrady) * 0.1
df.loc[(df.Year == 2015) & (df.Topic == "理科") & (df.Score < boundary),'Label']  += 1
boundary = np.max(T.values[T.values < boundary])
