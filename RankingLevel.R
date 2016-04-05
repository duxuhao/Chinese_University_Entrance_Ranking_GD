Dataset <- read.csv("UniversityData.csv")

Ranking <- c("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z") #level label
Ranking2 <- c(1:50)
N <- 11 # level quantity, control the step
B <- 2 # control step
T <- (B^((1:N))) / (B^ N)
Range <- c(0,T)

Level <- Dataset$Lowest_Ranking
for (i in 1:N+1) {
	Level[Dataset$Ranking_Percentage <= Range[i] & Dataset$Ranking_Percentage > Range[i-1] ] <- Ranking[i-1]
	}

Dataset <- cbind(Dataset, Level)
UniversityLevel <- Dataset[,c("Year","University_Name_Location","Province","Topic","Plan_Number", "GDP_Per_Person", "X1A_Number","Level")]
write.csv(UniversityLevel, "UniversityLevel.csv")


## train with machine learning

library(caret)
Science <- UniversityLevel[UniversityLevel$Topic == "理科",]
set.seed(1992912)
inTrain <- createDataPartition(y = Science$Level,p=0.7,list=FALSE)
Training <- Science[inTrain,]
Testing <- Science[-inTrain,]

#decision tree
library(rpart)
fit <- rpart(Level ~ ., method ="class",data = Training)
opt <- witch.min(fit$cptable[,"xerror"])
cp <- fit$cptable[opt,"CP"]
fit_prune <- prune(fit, cp = cp)
plot(fit_prune)
text(fit_prune, use.n=T)
pre <- predict(fit,newdata=Testing)
pre_prune <- predict(fit_prune, newdata=Testing)
performance <- confusionMatrix(pre,Testing$Level)
print(performance)
performance_prune <- confusionMatrix(pre_prune,Testing$Level)
print(performance_prune)

#random forest
library(randomForest)
ran <- randomForest(Level ~ ., data = Training, importance=TRUE, ntree = 10000)
print(ran)
ran_pre <- predict(ran, data = Testing)
table(observed = Testing$Level, predicted = ran_pre)

print(ran)
