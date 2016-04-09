import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt

df = pd.read_csv("UniversityData.csv") #kind of origin data
a = df[(df.Year == 2010) * (df.Topic == "理科")]
X = a[["UniversityNo","Ranking_Scores","Distance","Plan_Number","Lowest_Ranking"]]
X = a[["Ranking_Percentage","Lowest_Ranking"]]
