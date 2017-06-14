#SVM for letter analysis

alphabet <- read.csv("D:\\My Work\\Data Analysis\\dataset\\letterdata.csv")

str(alphabet)

alphabet_train <- alphabet [1 : (nrow(alphabet)*0.8),]
alphabet_test <- alphabet [(nrow(alphabet)*0.8):(nrow(alphabet)),]

#Fit in model kernlab
library(kernlab)

model_SVM <- ksvm(letter ~ . ,data =alphabet_train , kernel = "vanilladot")

model_SVM

SVM_pred <- predict(model_SVM,alphabet_test)

par(mfrow <- c(1,2))
table(SVM_pred,alphabet_test$letter, dnn = c("prdicted","actual"))

agreement <- SVM_pred == alphabet_test$letter

prop.table(table(agreement))*100

# Imporving the model using RFB kernel

model_SVM_rbf <- ksvm(letter ~ . ,data =alphabet_train , kernel = "rbfdot")

model_SVM_rbf

SVM_pred_rbf <- predict(model_SVM_rbf,alphabet_test)

par(mfrow <- c(1,2))
table(SVM_pred_rbf,alphabet_test$letter, dnn = c("prdicted","actual"))

agreement <- SVM_pred_rbf == alphabet_test$letter

prop.table(table(agreement))*100