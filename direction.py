import pandas as pd
import googlemaps
from datetime import datetime
import time
import numpy as np
import re

key = 'AIzaSyDVH4kBbF1fs6qVcEOeRuHoZlpdkhqIK18'
df = pd.read_csv("UniversityData.csv")
chinesename = pd.read_csv("Name_Pinyin.csv")
client = googlemaps.Client(key) #my google account key
origin = ["Guangzhou, China"] #my original location
name = df["University_Name"]
namelist = np.unique(name)
TT = open("distance.csv","a") #create the file

for i in range(namelist.shape[0]):
	desti =[namelist[i]]
	index = np.argmax(name == namelist[i])
	UniversityName = str(name[index:index+1])
	UniversityName = UniversityName[5:-37].strip()
	TT.write(UniversityName)
	try :
		T = client.distance_matrix(origin,desti)
		unidis = T["rows"][0]["elements"][0]["distance"]["text"]
		Distance = float(unidis[:-3].replace(",",""))
		TT.write(",")
		TT.write(str(Distance))
		TT.write("\n")
	except :
    		TT.write("\n")
TT.close()

