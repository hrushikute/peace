#Decision tree Algo rithm

#Step1 collecting Data


credit <- read.csv("D:\\My Work\\Data Analysis\\dataset\\credit.csv")

str(credit)

table(credit$checking_balance)
table(credit$savings_balance)


table(credit$default)

#Since the data is sorted and we need random value ..get the random index value from credit

set.seed(123)

train_sample <- sample(1000,900)

str(train_sample)

credit_train <- credit[train_sample,]
credit_test <- credit[-train_sample,]

prop.table(table(credit_train$default))

prop.table(table(credit_test$default))


# train the model on data
#install.packages("C50")
library(C50)


credit_model <- C5.0(credit_train[-17],factor(credit_train$default))

summary(credit_model)

credit_pred <- predict(credit_model,credit_test)

library(gmodels)

CrossTable(credit_test$default,credit_pred,prop.c = FALSE,
           prop.chisq = FALSE, prop.r = FALSE,
           dnn = c('actual default','predicted default'))

credit_boost <- C5.0(credit_train[-17],factor(credit_train$default),trials = 10)
credit_pred10 <- predict(credit_boost,credit_test)

CrossTable(credit_test$default,credit_pred10,prop.c = FALSE,
           prop.chisq = FALSE, 
           dnn = c('actual default','predicted default'))

matrix_dimensions <- list(c("no","yes"),c("no","yes"))
names(matrix_dimensions) <- c("predicted","actual")

matrix_dimensions
# define cost function to reduce the error percentage.
erro_Cost=matrix(c(0,1,4,0),nrow = 2)

erro_Cost

credit_cost <- C5.0(credit_train[-17],factor(credit_train$default),costs = erro_Cost)
credit_cost_pred <- predict(credit_cost,credit_test)
CrossTable(credit_test$default,credit_cost_pred,prop.c = FALSE,
           prop.chisq = FALSE,
           dnn = c('actual default','predicted default'))

