library(caret)

df <- read.csv("No_chinese_feature.csv")

Use <- df[,c("Year","UniversityNo","Ranking_Scores","Media_Impact","Plan_Number","X1A_Number","GDP_Per_Person","Lowest_Ranking")]
Use$Ranking_Scores[is.na(Use$Ranking_Scores)] <- 0
Use$Media_Impact[is.na(Use$Media_Impact)] <- 0
Use$GDP_Per_Person[is.na(Use$GDP_Per_Person)] <- 0

Use2 <- Use[Use$Lowest_Ranking > 10000 , ]
inTrain <- createDataPartition(y = Use2$Lowest_Ranking,p=0.8,list=FALSE)
Training <- Use2[inTrain,]
Testing <- Use2[-inTrain,]

mod <- train(Lowest_Ranking ~., method = "rf", data = Training)
pre <- predict(mod, newdata = Testing)
print(mod$finalModel)
plot(pre, Testing$Lowest_Ranking)
pre <- predict(mod, newdata = Use2)
plot(pre, Use2$Lowest_Ranking)

#prediction accuracy
N <- 0.15
Acc <- (abs(pre-Use2$Lowest_Ranking) / Use2$Lowest_Ranking)
print(sum(Acc<N)/length(pre))
hist(Acc,30)

