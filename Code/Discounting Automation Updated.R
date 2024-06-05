library(tidyverse)
library(readxl)
library(rio)
library(dplyr)
library(tidyr)
library(ChainLadder)
library(lubridate)
library(readr)
library(zoo)
library(ggplot2)

data_OS_2021 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/May/Discounting Automation/Data/Data.xlsx", 
                           sheet = "Raw Data_OS_21", col_types = c("text","date", "date", "text", "numeric","numeric", "numeric", "text", "numeric","numeric", "text", "numeric", "text", "text"))
data_OS_2022 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/May/Discounting Automation/Data/Data.xlsx", 
                           sheet = "Raw_Data_OS_22")
data_OS_2023 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/May/Discounting Automation/Data/Data.xlsx", 
                           sheet = "Raw_Data_OS_23")
data_Paid_2022 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/May/Discounting Automation/Data/Data.xlsx", 
                             sheet = "Raw_Data_Paid_22")
data_nse_yield_curve_2021 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/May/Discounting Automation/Data/Data.xlsx", 
                                        sheet = "NSE_Yield_Curve_2021")
data_nse_yield_curve_2022 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/May/Discounting Automation/Data/Data.xlsx", 
                                        sheet = "NSE_Yield_Curve_2022")  
data_nse_yield_curve_2023 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/May/Discounting Automation/Data/Data.xlsx", 
                                        sheet = "NSE_Yield_Curve_2023")


data_Paid_2022 <- data_Paid_2022 %>%
  mutate(
    Date.Regn = dmy(Date.Regn),
    Date.Loss = dmy(Date.Loss),
    Date.Paid = dmy(Date.Paid))

data_OS_2021 <- data_OS_2021 %>%
  mutate(
    Unique2 = if_else(duplicated(ClaimNo), 0, 1),
    Loss_Year = year(Date.Loss),
    Reported_Year = year(Date.Regn),
    Indicator_Claim_Type = ifelse(ClaimNo %in% data_OS_2022$ClaimNo, "Still_Outstanding", "Paid/Closed"),
    Loss_Yr_Loss_Qrt = paste0(year(Date.Loss), "Q", quarter(Date.Loss)),
    Not_in_Paid_File = ifelse(ClaimNo %in% data_Paid_2022$ClaimNo, 0, 1),
    Claim_Indicator = ifelse(Indicator_Claim_Type == "Still_Outstanding",ifelse(Not_in_Paid_File & (ClaimNo %in% data_OS_2022$ClaimNo & `OS Amount` == data_OS_2022$`OS Amount`[match(ClaimNo, data_OS_2022$ClaimNo)]),"A",ifelse(ClaimNo %in% data_Paid_2022$ClaimNo & ClaimNo %in% data_Paid_2022$ClaimNo,"B2","B1")),ifelse(ClaimNo %in% data_Paid_2022$ClaimNo,"C2","C1")),
    Indicator = paste(Loss_Year, Claim_Indicator, `IRA Class`, sep = ""))
 

data_Paid_2022 <- data_Paid_2022 %>%
  mutate(
    Loss_Year = year(Date.Loss),
    Report_Year = year(Date.Regn),
    Paid_Year = year(Date.Paid),
    Loss_Yr_Loss_Qrt = paste0(year(Date.Loss), "Q", quarter(Date.Loss)),
    Paid_Yr_Paid_Qrt = paste0(year(Date.Paid), "Q", quarter(Date.Paid)),
    Claim_Indicator = ifelse(ClaimNo %in% data_OS_2022$ClaimNo & ClaimNo %in% data_OS_2021$ClaimNo, ifelse(Loss_Year == 2022, "F1", "F2"), "Considered"))


View(data_Paid_2022)
View(data_OS_2021)

data_Paid_2022 <- data_Paid_2022 %>%
  group_by(ClaimNo) %>%
  mutate(Unique_ = ifelse(row_number() == 1, 1, 0))







#Claim Indicator Count, sum by OS Amount and Percentage 2021
claim_indicator_count_2021 <- data_OS_2021 %>%
  group_by(`Claim Indicator`) %>%
  summarise(count = n(), total_OS_Amount = sum(`OS Amount`)) %>%
  mutate(percentage = total_OS_Amount / sum(total_OS_Amount) * 100)

#Claim Indicator Count 2022
claim_indicator_count_2022 <- data_OS_2022 %>%
  group_by(`Claim Indicator`) %>%
  summarise(count = n(), total_OS_Amount = sum(`OS Amount`)) %>%
  mutate(percentage = count / sum(count) * 100)

#OS Amount summary by Class 2022
claim_indicator_sum_2022 <- data_OS_2022 %>%
  filter(`Claim Indicator`=='E1')%>%
  group_by(`IRA Class`) %>%
  summarize(total_OS_Amount = sum(`OS Amount`))

#Paid Claims 2022
Paid_claims_indicator_count_sum_2022 <- data_Paid_2022 %>%
  group_by(`Claim Indicator`) %>%
  summarise(count = n(), total_Gross_Paid = sum(`Gross Paid`))

#By Claim Indicator
Paid_Final_claims_indicator_count_sum_2022 <- data_Paid_2022 %>%
  group_by(`Final Claim Indicator`) %>%
  summarise(count = n(), total_Gross_Paid = sum(`Gross Paid`)) 

#Paid Claims 2022
#By Loss Year
Paid_claims_Loss_year_count_sum_2022 <- data_Paid_2022 %>%
  filter(`Revised Claim Indicator`=='B2')%>%
  group_by(`Loss Year`) %>%
  summarise(count = n(), total_Gross_Paid = sum(`Gross Paid`))

#Experience Adjustment
#2022 - OS claims by Loss Year
OS_claims_by_Loss_Year_2022 <- data_OS_2022 %>%
  group_by(`Loss Year`) %>%
  summarise(total_OS_Amount_2022 = sum(`OS Amount`))

#2023 - OS claims by Loss Year
OS_claims_by_Loss_Year_2023 <- data_OS_2023 %>%
  group_by(`Loss Year`) %>%
  summarise(total_OS_Amount_2023 = sum(`OS Amount`))













#OS Claims by IRA CLASS
OS_claims_by_IRA_Class <- data_OS_2023 %>%
  group_by(`IRA Class`) %>%
  summarise(total_OS_Amount = sum(`OS Amount`))

#OS Claims by IRA CLASS for 2023
OS_claims_by_IRA_Class_2023 <- data_OS_2023 %>%
  filter(`Loss Year` == 2023) %>%
  group_by(`IRA Class`) %>%
  summarise(total_OS_Amount_2023 = sum(`OS Amount`))








