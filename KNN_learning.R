#Get the library
#install.packages("class")
library(class)
library(gmodels)
#KNN algorithm
# Step 1 : Get data
wbcd <- read.csv("D:\\My Work\\Data Analysis\\dataset\\wisc_bc_data.csv",stringsAsFactors = FALSE)




#step 2 : explore and filter and normalize and prepare the data


str(wbcd)
typeof(wbcd)
#summary(wbcd)
# Always remove ID

wbcd <- wbcd[-1]

table(wbcd$diagnosis)
wbcd$diagnosis <- factor(wbcd$diagnosis,levels = c("B","M"),labels = c("Benign","Malignant"))

round(prop.table(table(wbcd$diagnosis))*100,digits=1)

summary(wbcd[c("radius_mean","area_mean","smoothness_mean")])

#normalize the data

normalize <- function(x){
  
  return((x-min(x))/(max(x)-min(x)))
}

wbcd_n <- as.data.frame(lapply(wbcd[2:31],normalize))

summary(wbcd_n[c("radius_mean","area_mean","smoothness_mean")])

# split the data in train and test

wbcd_train <- wbcd_n[1:469,]
wbcd_test <- wbcd_n[470:569,]


#target variable data set 

wbcd_train_labels <- wbcd[1:469,1]
wbcd_test_labels <- wbcd[470:569,1]




# Step 3 : Training model on data.

wbcd_test_pred <- knn(train = wbcd_train,test = wbcd_test, cl=wbcd_train_labels, k = 21)

# evaluate model performace

CrossTable(x=wbcd_test_labels,y=wbcd_test_pred,prop.chisq = FALSE)
