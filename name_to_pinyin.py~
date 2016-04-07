import pinyin
import pandas as pd
df = pd.read_csv("UniversityData.csv")
Name = df["University_Name"]

for i in range(len(Name)):
	Name[i] = pinyin.get(Name[i],format="strip")

df.to_csv("Name_Pinyin.csv")

