library(caret)
library(plotly)

Dataset <- read.csv("UniversityDataUsed.csv")
#Dataset <- Dataset[!is.na(Dataset$Lowest_Ranking),]
Dataset[,7] <- as.numeric(Dataset[,7])


Pro <- unique(Dataset["Province"])
Year <- unique(Dataset["Year"])
University <- unique(Dataset["University_Name"])
Topic <- unique(Dataset["Topic"])

DF <- Dataset[,c("Province","Year","Plan_Number")]

PlanProvince <- aggregate(DF$Plan_Number,by=list(DF$Province,DF$Year),FUN=sum)
colnames(PlanProvince) <- c("Province","Year","Planned_Quantity_for_enrolling")

NoGD <- PlanProvince[PlanProvince$Province!=PlanProvince$Province[10],]
ggplot(NoGD,aes(x=Province,y=Planned_Quantity_for_enrolling,fill=as.factor(Year),width=0.8)) + geom_bar(stat="identity", position="dodge")

GD <- PlanProvince[PlanProvince$Province==PlanProvince$Province[10],]
ggplot(GD,aes(x=Year,y=Planned_Quantity_for_enrolling)) + geom_bar(stat="identity")

Eco <- unique(cbind(Dataset[,c("Year","Province")],Dataset$GDP / Dataset$Population))


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
