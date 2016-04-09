Dataset <- read.csv("UniversityData.csv")
df <- read.csv("UniversityMarks.csv")
colnames(df) <- c("University_Name_Location","Year","Lowest","Highest","ave","Plan","NO","Topic")
df <- df[df$NO == "第一批",]
df$Highest[is.na(df$Highest)] = 10000
df$ave[is.na(df$ave)] = 10000
df$Lowest[is.na(df$Lowest)] = 10000
Score_Last_Year = apply(df[,3:5],1,min)
#Score_Last_Year = df$Lowest
New <- cbind(df[c("University_Name_Location","Year","Topic")],Score_Last_Year)
New$Year <- New$Year + 1
NDS <- merge(Dataset, New, all.X = TRUE)
write.csv(NDS, "UniversityDataTemp2.csv")
