# Regression algorithm to predict the cost of medical expenditure

insurance <- read.csv("D:\\My Work\\Data Analysis\\dataset\\insurance.csv")

str(insurance)

summary(insurance)

hist(insurance$charges)
table(insurance$region)
cor(insurance[c("age","bmi","children","charges")])

pairs(insurance[c("age","bmi","children","charges")])

library(psych)

pairs.panels(insurance[c("age","bmi","children","charges")])

ins_model <- lm(charges ~ .,data = insurance)

summary(ins_model)

#Adding non liner relationship
#Treatment charges may become disproportionately expensive for old population
insurance$age2 <- insurance$age^2
# feature creation by converting a numeric variable to a binary indidicator
insurance$bmi30 <- ifelse(insurance$bmi > 30,1,0)


#adding interaction effect (when 2 effects have combined effect is called interaction)

ins_model2 <- lm(charges ~ age + age2 + children + bmi + sex + bmi30*smoker + region ,data = insurance)

summary(ins_model2)

