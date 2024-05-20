library(tidyverse)
library(dplyr)

rm(list = ls())
setwd("C:/Users/Antonio/midirectorioGEO/RSpatialTutorial/")


## ------------------------------------------
## Cargamos el DataFrame
data <- read.csv2("data/LondonCustomer.csv")
str(data)
# View(data)


## ---------------------------------------------
## Limpiamos el DataFrame - Eliminamos las columnas que no utilizaremos
newData <- select(data, -FAMILYSIZE, -YEAREXPERIENCE, -ANNUALINCOME, -EDUCATIONLEVEL_ID)


## ----------------------------------------------
## Filtramos por los que tengan menos de 55 anios
newData <- newData[newData$AGE < 55, ]


## --------------------------------------------------------------------------
## Sumamos columnas NETPRICE y totalizamos en columna nueva -> volumenNegocio
newData$volumenNegocio <- rowSums(newData[, 3:9])

## Eliminamos columnas NETPRICE
newData <- select(newData, -NETPRICE_PRO11_AMT, -NETPRICE_PRO12_AMT, -NETPRICE_PRO13_AMT, -NETPRICE_PRO14_AMT, -NETPRICE_PRO15_AMT, -NETPRICE_PRO16_AMT, -NETPRICE_PRO17_AMT)

## Contamos el consumo por Distrito
menorConsumo <- aggregate(newData$volumenNegocio, by = list(newData$name), FUN=length)

## Ordenamos para visualizar los que menos consumo tuvieron
menorConsumo <- menorConsumo[order(menorConsumo[, 2]), ]
colnames(menorConsumo) <- c("Distrito", "ConsumoTotal")
View(menorConsumo)
#
#
## ---------------------------------------------------------------------------
## CASO #1
## Sabemos entonces que en base a la clientela menor a 55 anios, las oficinas
## con menor consumo de negocio son:
## City of London (2), Wandsworth (3), Ealing (10)
## ---------------------------------------------------------------------------