



library(ggplot2)

cars

ggplot(cars,aes(x=speed,y=dist))+geom_point(col='red')