library("xlsx")

fileScience <- "ScienceAdmissionScore.xlsx"
fileLiberalArt <- "LiberalArtAdmissionScore.xlsx"

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
	Temp <- cbind(as.character(ScienceName), rep("Science",dim(ScienceFile)[1]), SciencePlan, ScienceLowest, rep(a,dim(ScienceFile)[1]))
	Temp2 <- cbind(as.character(LiberalArtName), rep("LiberalArt",dim(LiberalArtFile)[1]), LiberalArtPlan, LiberalArtLowest, rep(a,dim(LiberalArtFile)[1]))
	T <- rbind(Temp, Temp2)
	UniversityAdmission <- rbind(UniversityAdmission,T)
}

colnames(UniversityAdmission) <- c("University_Name","Topic", "Plan_Number", "Lowest_Ranking", "Year")

MediaReportQuantity <- data.frame(UniversityName = as.character(),
				Province = as.character(),
				MeadiaReportNumber = as.numeric(),
				Year = as.numeric())

GDP <- data.frame(CityName = as.character(),
		GDPNumber = as.numeric(),
		Year = as.numeric())

Ranking <- data.frame(UNiversityName = as.character(),
		Ranking = as.numeric(),
		Year = as.numeric())
file1 <- "CuaaMediaRanking.xlsx" # The media impact factor
file2 <- "GDP.xlsx" # the GDP of different city
file3 <- "CuaaQualityRanking.xlsx" # the school ranking

for (a in 2009:2015) {
	Media <- read.xlsx(file1, sheetIndex=as.character(a))
	GDPData <- read.xlsx(file2, sheetIndex=as.character(a))
	RankingData <- read.xlsx(file3, sheetIndex=as.character(a))
	CityName <- GDPData$城市
	UniName <- Media$学校
	Province <- Media$所在
	
	UniversityName <- RankingData$学校
	CityGDP <- GDPData$GDP
	RankingScore <- RankingData$总分
	if (length(grep("新闻",names(Media))) != 0) {
		Quantity <- Media$新闻
	} else {Quantity <- Media$得分
	}
	
	Quantity <- Quantity/Quantity[1]
	Temp <- cbind(as.character(UniName), as.character(Province), Quantity, rep(a,dim(Media)[1]))
	MediaReportQuantity <- rbind(MediaReportQuantity,Temp)
	Temp2 <- cbind(as.character(CityName), CityGDP, rep(a,dim(GDPData)[1]))
	GDP <- rbind(GDP,Temp2)
	Temp3 <- cbind(as.character(UniversityName), RankingScore, rep(a,dim(RankingData)[1]))
	Ranking <- rbind(Ranking,Temp3)
}

colnames(MediaReportQuantity) <- c("University_Name","Province","Media_Impact", "Year")
colnames(GDP) <- c("City_Name","GDP", "Year")
colnames(Ranking) <- c("University_Name","Ranking_Scores", "Year")

TempT <- merge(UniversityAdmission, Ranking,all.x=TRUE)
UniversityData <- merge(TempT,MediaReportQuantity,all.x = TRUE)