library("xlsx")

file <- "CuaaMediaRanking.xlsx"
Media <- read.xlsx(file, sheetIndex="2014")
