# For obtaining the origin dataset
library("xlsx")

fileScience <- "Original_Data//ScienceAdmissionScore.xlsx" #the file contain the science student enrollment information
fileLiberalArt <- "Original_Data//LiberalArtAdmissionScore.xlsx" #the file contain the liberal art student enrollment information
StudentNum <- read.csv("Original_Data//StudentPopulation.csv") #the student population in GUangdong each year

UniversityAdmission <- data.frame(UNiversityName = as.character(),
		UniversityNo = as.character(),
		Topic = as.character(),
		Plan = as.numeric(),
		Lowest = as.numeric(),
		Score = as.numeric(),
		Year = as.numeric())


for (a in 2010:2015) {
	ScienceFile <- read.xlsx(fileScience, sheetIndex=as.character(a))	
	LiberalArtFile <- read.xlsx(fileLiberalArt, sheetIndex=as.character(a))
	ScienceName <- ScienceFile$院校名称
	LiberalArtName <- LiberalArtFile$院校名称
	ScienceScore <- ScienceFile$投档分
	LiberalArtScore <- LiberalArtFile$投档分
	if (a == 2010) { # there is different university label in 2010
		ScienceNo <- ScienceFile$院校号
		LiberalArtNo <- LiberalArtFile$院校号
		} else {
		ScienceNo <- ScienceFile$院校代码
		LiberalArtNo <- LiberalArtFile$院校代码
		}
	SciencePlan <- ScienceFile$计划
	LiberalArtPlan <- LiberalArtFile$计划
	ScienceLowest <- ScienceFile$最低
	LiberalArtLowest <- LiberalArtFile$最低
	Temp <- cbind(as.character(ScienceName), as.character(ScienceNo),rep("理科",dim(ScienceFile)[1]), SciencePlan, as.character(ScienceLowest),as.character(ScienceScore), rep(a,dim(ScienceFile)[1]))
	Temp2 <- cbind(as.character(LiberalArtName), as.character(LiberalArtNo),rep("文科",dim(LiberalArtFile)[1]), LiberalArtPlan, as.character(LiberalArtLowest),as.character(LiberalArtScore), rep(a,dim(LiberalArtFile)[1]))
	T <- rbind(Temp, Temp2)
	UniversityAdmission <- rbind(UniversityAdmission,T)
}

colnames(UniversityAdmission) <- c("University_Name_Location","UniversityNo","Topic", "Plan_Number", "Lowest_Ranking","Score","Year")

MediaReportQuantity <- data.frame(UniversityName = as.character(),
				MeadiaReportNumber = as.numeric(),
				Year = as.numeric())

GDP <- data.frame(CityName = as.character(),
		GDPNumber = as.numeric(),
		Year = as.numeric())

Population <- data.frame(CityName = as.character(),
		Population = as.numeric(),
		Year = as.numeric())

Ranking <- data.frame(UniversityName = as.character(),
		Ranking = as.numeric(),
		Year = as.numeric())

file1 <- "Original_Data//CuaaMediaRanking.xlsx" # The media impact factor
file2 <- "Original_Data//ProvinceGDP2.xlsx" # the GDP of different city
file3 <- "Original_Data//CuaaQualityRanking.xlsx" # the school ranking
file4 <- "Original_Data//TotalPopulation.xlsx" # the province population

for (a in 2009:2014) {
	Media <- read.xlsx(file1, sheetIndex=as.character(a))
	GDPData <- read.xlsx(file2, sheetIndex=as.character(a))
	RankingData <- read.xlsx(file3, sheetIndex=as.character(a))
	PopulationD <- read.xlsx(file4, sheetIndex=as.character(a))
	PopulationD[,1] <- gsub("[[:blank:]]","",PopulationD[,1])
	CityName <- GDPData$地区
	UniName <- Media$学校
	CityP <- PopulationD$地区
	people <- PopulationD$人口
	
	
	UniversityName <- RankingData$学校
	CityGDP <- GDPData$本币
	RankingScore <- RankingData$总分
	if (length(grep("新闻",names(Media))) != 0) {
		Quantity <- Media$新闻
	} else {Quantity <- Media$得分
	}
	n <- a + 1 #when n == a, it means the data we use is the same year with the admission year, when n == a + 1, it means the data we use is the previous yea

	Quantity <- Quantity/Quantity[1]
	Temp <- cbind(as.character(UniName),  Quantity, rep(n,dim(Media)[1]))
	MediaReportQuantity <- rbind(MediaReportQuantity,Temp)
	Temp2 <- cbind(as.character(CityName), CityGDP, rep(n,dim(GDPData)[1]))
	
	GDP <- rbind(GDP,Temp2)
	Temp3 <- cbind(as.character(UniversityName), RankingScore, rep(n,dim(RankingData)[1]))
	Ranking <- rbind(Ranking,Temp3)
	
	Temp4 <- cbind(as.character(CityP), people, rep(n,dim(PopulationD)[1]))
	Population <- rbind(Population, Temp4)
	
}

UniversityLocation <- read.xlsx("Original_Data//UniversityLocation.xlsx", sheetIndex=1)
UniversityLocation <- unique(UniversityLocation)
colnames(UniversityLocation) <- c("Province","University_Name_Location")


colnames(MediaReportQuantity) <- c("University_Name","Media_Impact", "Year")
colnames(GDP) <- c("Province","GDP", "Year")
colnames(Ranking) <- c("University_Name","Ranking_Scores", "Year")
colnames(Population) <- c("Province","Population", "Year")

#since some universities are named with their campus name, so we need to obtain the original university name
UnivName <- UniversityAdmission$University_Name_Location
UnivName <- sub("大学", "大学.o", UnivName)
UnivName <- sub("学院", "学院.o", UnivName)
T <- unlist(strsplit(UnivName,"\\."))
University_Name <- matrix(T, nrow=2)[1,]
UniversityAdmission <- cbind(UniversityAdmission,University_Name)

#begin to merge the dataset
TempT <- merge(UniversityAdmission, Ranking,all.x=TRUE) #merge universities' ranking
TempT2 <- merge(TempT,MediaReportQuantity,all.x = TRUE) #merge universities' media impact
TempT3 <- merge(TempT2,UniversityLocation,all.x = TRUE) #merge universities' location
TempT4 <- merge(TempT3,GDP,all.x = TRUE) #merge provinces' GDP
UniversityData <- merge(TempT4,Population,all.x = TRUE) #merge provinces' population
UniversityData <- merge(UniversityData,StudentNum,all.x = TRUE) #merge paticipate student number in Guangdong

write.csv(UniversityData, "Produce_Data//UniversityDataTemp.csv") #produce the temp file for storing the first part data
Dataset <- read.csv("Produce_Data//UniversityDataTemp.csv")
Dataset$X <- NULL
GDP_Per_Person <- Dataset$GDP / Dataset$Population
UniversityData <- cbind(Dataset, GDP_Per_Person)
A1_Number <- read.csv("Original_Data//1AStudent.csv")
UniversityData <- merge(UniversityData, A1_Number, all.x=TRUE) #merge the 1A enroll student quantity
Ranking_Percentage <- UniversityData$Lowest_Ranking/UniversityData$X1A_Number #obtain the enroll percentage
UniversityData <- cbind(UniversityData, Ranking_Percentage)

Pinyin <- read.csv("Original_Data//Name_Pinyin.csv")
UniversityData <- merge(UniversityData, Pinyin,all.x=TRUE)
distance <- read.csv("Original_Data//distance.csv",header=F) #the distance file is obtain via google map service by python direction.py
colnames(distance) <- c("University_Name","Distance")
UniversityData <- merge(UniversityData, distance, all.x=TRUE)
UniversityData <- unique(UniversityData)
UniversityData$Media_Impact[is.na(UniversityData$Media_Impact)] <- 0 #no media report means 0 media impact
UniversityData$Ranking_Scores[is.na(UniversityData$Ranking_Scores)] <- 0 #no university ranking score means 0 ranking
write.csv(UniversityData, "Produce_Data//UniversityData.csv")
