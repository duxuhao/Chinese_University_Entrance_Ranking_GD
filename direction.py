import pandas as pd
import googlemaps
from datetime import datetime
import time
import numpy as np
import re

key = 'AIzaSyDVH4kBbF1fs6qVcEOeRuHoZlpdkhqIK18'
df = pd.read_csv("UniversityData.csv")
chinesename = pd.read_csv("Name_Pinyin.csv")
client = googlemaps.Client(key)
origin = ["Guangzhou, China"]
name = df["University_Name"]
namelist = np.unique(name)
TT = open("distance.csv","a")
'''
for i in range(name.shape[0]):
	desti =[namelist[i]]
	TT.write(str(desti)[2:-2])
	try :
		desti =[namelist[i]]
		T = client.distance_matrix(origin,desti)
		unidis = T["rows"][0]["elements"][0]["distance"]["text"]
		Distance = int(filter(str.isdigit,str(unidis)))
		TT.write(",")
		TT.write(str(Distance))
		TT.write("\n")
	except :
    		TT.write("\n")

TT.close()
'''
for i in range(namelist.shape[0]):
#for i in range(2):
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

