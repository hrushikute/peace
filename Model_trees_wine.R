#  model tress and regression tree and model tree for predicting the quality of wine

# step 1 collect the data
wine <- read.csv("D:\\My Work\\Data Analysis\\dataset\\whitewines.csv")

str(wine)

hist(wine$quality)

#2: Exploring and prepating the data

wine_train <- wine[1:(nrow(wine)*0.75), ]
wine_test <- wine[((nrow(wine)*0.75)):nrow(wine), ]

#3: Trainig a regresssion tree model model on the data.
#install.packages(rpart) # RPAT is used for recurrsive partitoioning.
library(rpart)
model_reg_tree <- rpart(quality ~ .,data = wine_train)

summary(model_reg_tree)

model_reg_tree

#install.packages("rpart.plot")
library(rpart.plot)

rpart.plot(model_reg_tree,digits = 3,fallen.leaves = TRUE,type = 3,extra = 101)
pred <- predict(model_reg_tree,wine_test)

summary(pred)
summary(wine_test$quality)

# test model performace
cor(pred,wine_test$quality)

library(Metrics)

mae(pred,wine_test$quality)

#improving the regression tree model with model tree uing M5 in RWEka
library(RWeka)
model_tree=M5P(quality ~ .,data =wine_train)
model_tree
summary(model_tree)

pred_m5p <- predict(model_tree,wine_test)

mae(pred_m5p,wine_test$quality)
