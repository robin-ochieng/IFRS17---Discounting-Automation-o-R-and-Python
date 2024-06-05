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

data_OS_2021 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                   sheet = "Raw Data_OS_21")
data_OS_2022 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                           sheet = "Raw_Data_OS_22")
data_OS_2023 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                           sheet = "Raw_Data_OS_23")
data_Paid_2022 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                             sheet = "Raw_Data_Paid_22")
data_nse_yield_curve_2021 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                                        sheet = "NSE_Yield_Curve_2021")
data_nse_yield_curve_2022 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                                        sheet = "NSE_Yield_Curve_2022")  
data_nse_yield_curve_2023 <- read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                                        sheet = "NSE_Yield_Curve_2023")

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








