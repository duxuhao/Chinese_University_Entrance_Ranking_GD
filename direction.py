import pandas as pd
import googlemaps
from datetime import datetime
import time
import numpy as np

key = 'AIzaSyDVH4kBbF1fs6qVcEOeRuHoZlpdkhqIK18'
df = pd.read_csv("UniversityData.csv")
client = googlemaps.Client(key)
origin = ["Guangzhou, China"]
name = df["University_Name"]
namelist = np.unique(name)
TT = open("distance.csv","a")
for i in range(name.shape[0]):
	index = np.argmax(name == namelist[i])
	UniversityName = str(name[index:index+1])
	TT.write(UniversityName[5:-37])
	TT.write(",")
	desti =[namelist[i]]
	T = client.distance_matrix(origin,desti)
	unidis = T["rows"][0]["elements"][0]["distance"]["text"]
	Distance = int(filter(str.isdigit,str(unidis)))
	TT.write(str(Distance))
	TT.write("\n")

TT.close()



