#Importing the libraries
import pandas as pd
import numpy as np
import xlwings as xw

#Import the datasets 
data_OS_2021 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", sheet_name = "Raw Data_OS_21")

data_OS_2022 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", sheet_name = "Raw_Data_OS_22")

data_OS_2023 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", sheet_name = "Raw_Data_OS_23")

data_Paid_2022 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", sheet_name = "Raw_Data_Paid_22")

# Load the workbook where the results will be recorded
wb = xw.Book('C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/May/Discounting Automation/Data/Data.xlsx')

# Select a sheet
sheet = wb.sheets['Reconciliation of OCR']

# Write data to the sheet
sheet.range('F5').value = data_OS_2021['OS Amount'].sum()

sheet.range('F6').value = data_Paid_2022['Gross Paid'].sum()

sheet.range('G17').value = data_Paid_2022['Gross Paid'].sum()

sheet.range('G18').value = data_Paid_2022.loc[data_Paid_2022['Final Claim Indicator'] == 'E2', 'Gross Paid'].sum()

sheet.range('G19').value = data_OS_2022.loc[data_OS_2022['Claim Indicator '] == 'E1', 'OS Amount'].sum()

sheet.range('G24').value = data_Paid_2022.loc[data_Paid_2022['Final Claim Indicator'] == 'F2', 'Gross Paid'].sum()

sheet.range('G25').value = data_Paid_2022.loc[data_Paid_2022['Final Claim Indicator'] == 'F3', 'Gross Paid'].sum()

sheet.range('G26').value = data_OS_2022.loc[data_OS_2022['Claim Indicator '] == 'D', 'OS Amount'].sum()

sheet.range('G31').value = data_OS_2021.loc[data_OS_2021['Claim Indicator '] == 'C2', 'OS Amount'].sum()

sheet.range('G32').value = (data_Paid_2022.loc[data_Paid_2022['Final Claim Indicator'] == 'C2', 'Gross Paid'].sum())-(data_OS_2021.loc[data_OS_2021['Claim Indicator '] == 'C2', 'OS Amount'].sum())

sheet.range('G33').value = data_Paid_2022.loc[data_Paid_2022['Final Claim Indicator'] == 'B2', 'Gross Paid'].sum()

sheet.range('G37').value = (data_OS_2022.loc[data_OS_2022['Claim Indicator '] == 'B1', 'OS Amount'].sum())-(data_OS_2021.loc[data_OS_2021['Claim Indicator '] == 'B1', 'OS Amount'].sum())

sheet.range('G38').value = (data_OS_2022.loc[data_OS_2022['Claim Indicator '] == 'B2', 'OS Amount'].sum())-(data_OS_2021.loc[data_OS_2021['Claim Indicator '] == 'B2', 'OS Amount'].sum())

sheet.range('G39').value = data_OS_2021.loc[data_OS_2021['Claim Indicator '] == 'C1', 'OS Amount'].sum()

sheet.range('F45').value = data_OS_2022['OS Amount'].sum()

# Save the workbook
wb.save()