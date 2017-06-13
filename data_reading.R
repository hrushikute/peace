car <- read.csv(file="D:\\My Work\\Data Analysis\\Used_cars.csv")

car <- na.omit(car)

print (car)

str(car)

summary(car)

summary(car[c("price","mileage")])
typeof(car)
range(car$price)
diff(range(car$price))
IQR(car$price)
quantile(car$price)

#Box plot 
par(mfrow=c(1,2))
boxplot(car$price,main = "Box plot of used car prices",ylab="Price($)")
boxplot(car$mileage,main = "Box plot of used car Mileage",ylab="Odometer (mi.)")

#histogram
par(mfrow=c(1,2))
hist(car$price,main="Histogram of Used car Price",xlab = "Price($)")
hist(car$mileage,main="Histogram of Used car Price",xlab = "Odometer(mi)")

#Variance and standard deviation
var(car$price)
sd(car$price)
var(car$mileage)
sd(car$mileage)

# Function to anylyse categorical data

table(car$year)
table(car$model)
table(car$color)

#calculate the proportion directly 

model_table <- table(car$model)
prop.table(model_table)

color_pct <- table(car$color)
color_pct <- prop.table(color_pct)*100
round(color_pct,digits = 1)


#Visualizing the relationships.
# We are taki9ng price at Y axis(dependent variable)  as prices depend upon odometer reading or mileage
par(mfrow=c(1,1))
plot(x = car$mileage ,y = car$price,
     main = " Scatter plot of Price Vs Mileage",
     xlab = "Used car Odometer (mi.)",
     ylab = "Usef car Price ($)")


#Examining realtionships - two way cross tabulation - or con
#install.packages("gmodels")
library(gmodels)

#divinding color of car as conservative or not. OCnservative in clude "Black White Gray silver" 1 is True and 0 is false

car$conservative <- car$color %in% c("Black","Gray","Silver","White")

table(car$conservative)

#cross tabluation as conservative color indicator at Y axis

CrossTable(x=car$model,y=car$conservative,chisq = TRUE)