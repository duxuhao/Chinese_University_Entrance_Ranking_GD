library(caret)

Dataset <- read.csv("UniversityDataPreviousYearPrediction.csv")
Dataset <- Dataset[!is.na(Dataset$Lowest_Ranking),]
Dataset[,7] <- as.numeric(Dataset[,7])
Science <- Dataset[Dataset$Topic == "理科",]
set.seed(1992912)
inTrain <- createDataPartition(y = Science$X,p=0.7,list=FALSE)
Training <- Science[inTrain,]
Testing <- Science[-inTrain,]

mod <- train(Lowest_Ranking ~ ., method='rf',data=Training)
pre <- predict(mod,newdata=Testing)
performance <- confusionMatrix(pre,Testing$class)
