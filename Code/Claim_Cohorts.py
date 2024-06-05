#Importing the libraries
import pandas as pd
import numpy as np
import xlwings as xw

#Import the datasets 
data_OS_2022 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/May/Discounting Automation/Data/Data_2024.xlsx", sheet_name = "Raw Data_OS_22")

data_OS_2023 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/May/Discounting Automation/Data/Data_2024.xlsx", sheet_name = "Raw_Data_OS_23")

data_OS_2024 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/May/Discounting Automation/Data/Data_2024.xlsx", sheet_name = "Raw_Data_OS_24")

data_Paid_2023 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/May/Discounting Automation/Data/Data_2024.xlsx", sheet_name = "Raw_Data_Paid_23")

# Load the workbook where the results will be recorded
wb = xw.Book('C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/May/Discounting Automation/Data/Data_2024.xlsx')

# Select a sheet
sheet = wb.sheets['2021 OCR Cohorts']


# Define the columns by their names based on your description
indicator_column = 'Indicator'
os_amount_column = 'OS Amount'

# Define the year column and IRA class from user's description
year_column = 'Loss Year'
ira_class = 'Workmen\'s Compensation'  # this value seems fixed for now

# Get unique years from the year column for years >= 2009
years = data_OS_2022[data_OS_2022[year_column] >= 2009][year_column].unique()

# Prepare a DataFrame to hold the results
results = pd.DataFrame(index=[f'A_{ira_class}', f'B1_{ira_class}', f'B2_{ira_class}', f'C1_{ira_class}', f'C2_{ira_class}'])

# Iterate through the years and calculate the sums
for year in years:
    year = int(year)  # Ensure the year is an integer
    # Construct the indicator for each class and sum the 'OS Amount' where the conditions meet
    for class_label in results.index:
        condition = f"{year}{class_label.replace(f'_{ira_class}', '')}{ira_class}"
        results.loc[class_label, year] = data_OS_2022.loc[
            data_OS_2022[indicator_column] == condition, os_amount_column].sum()

# Display the resulting table
print(results)




results.to_excel("C:/Users/Robin Ochieng/Desktop/Data/daya.xlsx")

data_OS_2022[(data_OS_2022['Indicator'] == 2022 + "A" + "Workmen's Compensation")]['OS Amount'].sum()

# Convert the integer 2022 to a string and concatenate with other strings
indicator_value = str(2022) + "A" + "Workmen's Compensation"

# Now use this string to filter and sum the 'OS Amount'
sum_os_amount = data_OS_2022[data_OS_2022['Indicator'] == indicator_value]['OS Amount'].sum()



