Dataset <- read.csv("UniversityData.csv")

Ranking <- c("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z") #level label
N <- 25 # level quantity, control the step
B <- 1.4 # control step
T <- (B^((1:N)-0.5)) / (B^ (N - 0.5))
Range <- c(0,T)

Level <- Dataset$Lowest_Ranking
for (i in 1:N+1) {
	Level[Dataset$Ranking_Percentage <= Range[i] & Dataset$Ranking_Percentage > Range[i-1] ] <- Ranking[i]
	}

Dataset <- cbind(Dataset, Level)
UniversityLevel <- Dataset[,c("Year","University_Name_Location","Province","Topic","Plan_Number", "GDP_Per_Person", "X1A_Number","Level")]
write.csv(UniversityLevel, "UniversityLevel.csv")


## train with machine learning
Science <- UniversityLevel[UniversityLevel$Topic == "理科",]
set.seed(1992912)
inTrain <- createDataPartition(y = Science$Level,p=0.7,list=FALSE)
Training <- Science[inTrain,]
Testing <- Science[-inTrain,]

mod <- train(Level ~ ., method='rf',data=Training)
pre <- predict(mod,newdata=Testing)
performance <- confusionMatrix(pre,Testing$class)
