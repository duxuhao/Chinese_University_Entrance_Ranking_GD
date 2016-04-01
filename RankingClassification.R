library(caret)
library(plotly)

Dataset <- read.csv("UniversityDataPreviousYearPrediction.csv")
Dataset <- Dataset[!is.na(Dataset$Lowest_Ranking),]
Dataset[,7] <- as.numeric(Dataset[,7])


Pro <- unique(Dataset["Province"])
Year <- unique(Dataset["Year"])
University <- unique(Dataset["University_Name"])
Topic <- unique(Dataset["Topic"])

DF <- Dataset[,c("Topic","Province","Year","Plan_Number")]

PlanProvince <- aggregate(DF$Plan_Number,by=list(DF$Topic,DF$Province,DF$Year),FUN=sum)


if(FALSE) {
Science <- Dataset[Dataset$Topic == "理科",]
set.seed(1992912)
inTrain <- createDataPartition(y = Science$X,p=0.7,list=FALSE)
Training <- Science[inTrain,]
Testing <- Science[-inTrain,]

mod <- train(Lowest_Ranking ~ ., method='rf',data=Training)
pre <- predict(mod,newdata=Testing)
performance <- confusionMatrix(pre,Testing$class)
}
