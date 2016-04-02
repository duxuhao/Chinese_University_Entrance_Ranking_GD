library("xlsx")

fileScience <- "ScienceAdmissionScore.xlsx"
fileLiberalArt <- "LiberalArtAdmissionScore.xlsx"
StudentNum <- read.csv("StudentPopulation.csv")

UniversityAdmission <- data.frame(UNiversityName = as.character(),
		Topic = as.character(),
		Plan = as.numeric(),
		Lowest = as.numeric(),
		Year = as.numeric())


for (a in 2010:2015) {
	ScienceFile <- read.xlsx(fileScience, sheetIndex=as.character(a))	
	LiberalArtFile <- read.xlsx(fileLiberalArt, sheetIndex=as.character(a))
	ScienceName <- ScienceFile$院校名称
	LiberalArtName <- LiberalArtFile$院校名称
	SciencePlan <- ScienceFile$计划
	LiberalArtPlan <- LiberalArtFile$计划
	ScienceLowest <- ScienceFile$最低
	LiberalArtLowest <- LiberalArtFile$最低
	Temp <- cbind(as.character(ScienceName), rep("理科",dim(ScienceFile)[1]), SciencePlan, as.character(ScienceLowest), rep(a,dim(ScienceFile)[1]))
	Temp2 <- cbind(as.character(LiberalArtName), rep("文科",dim(LiberalArtFile)[1]), LiberalArtPlan, as.character(LiberalArtLowest), rep(a,dim(LiberalArtFile)[1]))
	T <- rbind(Temp, Temp2)
	UniversityAdmission <- rbind(UniversityAdmission,T)
}

colnames(UniversityAdmission) <- c("University_Name","Topic", "Plan_Number", "Lowest_Ranking", "Year")

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

file1 <- "CuaaMediaRanking.xlsx" # The media impact factor
file2 <- "ProvinceGDP2.xlsx" # the GDP of different city
file3 <- "CuaaQualityRanking.xlsx" # the school ranking
file4 <- "TotalPopulation.xlsx" #
file5 <- "StudentPopulation.xlsx" #

for (a in 2009:2014) {
	Media <- read.xlsx(file1, sheetIndex=as.character(a))
	GDPData <- read.xlsx(file2, sheetIndex=as.character(a))
	RankingData <- read.xlsx(file3, sheetIndex=as.character(a))
	PopulationD <- read.xlsx(file4, sheetIndex=as.character(a))
	Student <- read.xlsx(file5, sheetIndex=as.character(a))
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

UniversityLocation <- read.xlsx("UniversityLocation.xlsx", sheetIndex=1)
UniversityLocation <- unique(UniversityLocation)
colnames(UniversityLocation) <- c("Province","University_Name")


colnames(MediaReportQuantity) <- c("University_Name","Media_Impact", "Year")
colnames(GDP) <- c("Province","GDP", "Year")
colnames(Ranking) <- c("University_Name","Ranking_Scores", "Year")
colnames(Population) <- c("Province","Population", "Year")

TempT <- merge(UniversityAdmission, Ranking,all.x=TRUE)
TempT2 <- merge(TempT,MediaReportQuantity,all.x = TRUE)
TempT3 <- merge(TempT2,UniversityLocation,all.x = TRUE)
TempT4 <- merge(TempT3,GDP,all.x = TRUE)
UniversityData <- merge(TempT4,Population,all.x = TRUE)
UniversityData[,7] <- as.numeric(UniversityData[,7])

UniversityData <- merge(UniversityData,StudentNum,all.x = TRUE)

#write.csv(UniversityData, "UniversityData.csv")
write.csv(UniversityData, "UniversityDataUsed.csv")
Dataset <- read.csv("UniversityDataUsed.csv")
GDP_Per_Person <- Dataset$GDP / Dataset$Population
UniversityData <- cbind(Dataset, GDP_Per_Person)
write.csv(UniversityData, "UniversityDataUsed.csv")
