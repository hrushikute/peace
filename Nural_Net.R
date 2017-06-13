#Nureal Network algo

# Step 1 : Collect the data

concrete <-  read.csv("D:\\My Work\\Data Analysis\\dataset\\concrete.csv")

str(concrete)

normal_func <- function(x){
  
  return((x-min(x))/(max(x)-min(x)))
}

concrete_norm <- as.data.frame(lapply(concrete,normal_func))

summary(concrete_norm)

concrete_train <- concrete_norm[1:(nrow(concrete_norm)*0.75), ]
concrete_test <- concrete_norm[((nrow(concrete_norm)*0.75)):nrow(concrete_norm), ]

#Train a neuralnet model
library(neuralnet)

concrete_model <- neuralnet(strength ~ cement + slag + ash + water + superplastic + coarseagg + 
                              fineagg + age, data = concrete_train)

plot(concrete_model)

model_result <- compute(concrete_model,concrete_test[1:8])
predicted_strength <- model_result$net.result

cor(predicted_strength,concrete_test$strength)



concrete_model2 <- neuralnet(strength ~ cement + slag + ash + water + superplastic + coarseagg + 
                              fineagg + age, data = concrete_train, hidden = 5)
plot(concrete_model2)

model_result2 <- compute(concrete_model2,concrete_test[1:8])
predicted_strength2 <- model_result2$net.result

cor(predicted_strength2,concrete_test$strength)