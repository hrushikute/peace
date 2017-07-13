# Titanic from kaggle


# step read the data from input file
Titanic_train=read.csv("D:\\My Work\\Data Analysis\\dataset\\kaggle\\Titanic\\train.csv")
Titanic_test =read.csv("D:\\My Work\\Data Analysis\\dataset\\kaggle\\Titanic\\test.csv")

Titanic_train.row <- 1:nrow(Titanic_train)
Titanic_test.row <- (1+nrow(Titanic_train)):(nrow(Titanic_train)+nrow(Titanic_test)) 

#Titanic_test$Survived <- rep("NA",Titanic_test$Name)
library(dplyr)
library(stringr)
library(rpart)
library(e1071)
library(partykit)
library(randomForest)
library(party)

Titanic_total <- bind_rows(Titanic_train,Titanic_test)




#Step 2: Crete features.

Titanic_total$Title= gsub('(.*, )|(\\..*)','',Titanic_total$Name)
table(Titanic_total$Sex, Titanic_total$Title)

Titanic_total$Title <- ifelse((Titanic_total$Title=="Mlle" | Titanic_total$Title=="Ms" | Titanic_total$Title=="Ms" |
                                 Titanic_total$Title=="Mme"),"Miss",Titanic_total$Title)
diffrent_Title <- c("Capt","Col", "Don", "Dona", "Dr", "Jonkheer", "Lady", "Major","Rev","Sir")

Titanic_total$Title [Titanic_total$Title %in% diffrent_Title] <- "Diff_Title"

Titanic_total$Title <- as.factor(Titanic_total$Title)



Titanic_total$Cabin <- sapply(Titanic_total$Cabin, function(x) str_sub(x,start=1,end=1))



Titanic_total$FamilySize <- Titanic_total$SibSp + Titanic_total$Parch +1

age.model <- rpart(Age ~ Pclass+Sex+SibSp+Parch+Fare+Embarked+Title, data=Titanic_total[!is.na(Titanic_total$Age), ],
                   method='anova')
Titanic_total$Age[is.na(Titanic_total$Age)] <- predict(age.model,Titanic_total[is.na(Titanic_total$Age), ])


Titanic_total[ is.na(Titanic_total$Fare),]

Titanic_total$Fare[is.na(Titanic_total$Fare)] <- median(Titanic_total[Titanic_total$Pclass=='3' & Titanic_total$Embarked=='S',]$Fare, na.rm=TRUE)
Titanic_total$Embarked[is.na(Titanic_total$Embarked)] <- 'C'
Titanic_total$Embarked <- as.factor(Titanic_total$Embarked)



set.seed(432)
# model <- cforest(Survived ~ Pclass+Title+Sex+Age+FamilySize+Fare+Embarked, data=Titanic_total[Titanic_train.row, ],
#                  controls=cforest_unbiased(ntree=2000, mtry=3))
# 
# pred <- predict(model,Titanic_total[Titanic_test.row,],OOB=TRUE, type = "response")
# pred <- ifelse(pred>0.5,1,0)
# output <- data.frame(PassengerId=Titanic_test$PassengerId, Survived = pred)

library(kernlab)
model_SVM <- ksvm(Survived ~ Pclass+Title+Sex+Age+FamilySize+Fare+Embarked,data =Titanic_total[Titanic_train.row, ]
                  , kernel = "rbfdot")
pred <- predict(model,Titanic_total[Titanic_test.row,],OOB=TRUE, type = "response")
pred <- ifelse(pred>0.5,1,0)
output <- data.frame(PassengerId=Titanic_test$PassengerId, Survived = pred)
write.csv(output,file = "D:\\My Work\\Data Analysis\\dataset\\kaggle\\Titanic\\output.csv", row.names = FALSE)