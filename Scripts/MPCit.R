##This script is for dealing with citation tables. Some times I dont know why, 
##the csv citation file obtained with CallsItemCitation.py code, adds more columns
##than desire, running this code over the csv file you solve that

library(dplyr)

setwd("")
data<-read.csv2(".csv",sep=",")
dataname<-".csv"

x<-which(colnames(data)=="author") #author is the first column of the real data
x<-x-1
x<-as.numeric(x)
data<-data[,-1:-x]

write.csv2(data,dataname)