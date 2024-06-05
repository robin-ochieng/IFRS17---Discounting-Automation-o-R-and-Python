import pandas as pd
import numpy as np

# Load the data from Excel sheets into pandas DataFrames
data_OS_2021 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                   sheet_name = "Raw Data_OS_21")
data_OS_2022 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                           sheet_name = "Raw_Data_OS_22")
data_OS_2023 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                           sheet_name = "Raw_Data_OS_23")
data_Paid_2022 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                             sheet_name = "Raw_Data_Paid_22")

# Load the NSE Yield Curve data from Excel sheets into pandas DataFrames
data_nse_yield_curve_2021 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                                        sheet_name = "NSE_Yield_Curve_2021")
data_nse_yield_curve_2022 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                                        sheet_name = "NSE_Yield_Curve_2022")  
data_nse_yield_curve_2023 = pd.read_excel("C:/Users/Robin Ochieng/OneDrive - Kenbright/Attachments/projects/2024/April/Discounting Automation/Data/Data.xlsx", 
                                        sheet_name = "NSE_Yield_Curve_2023")


# Define a function to check the status based on the claim number
def check_status(claim_no):
    return 'Paid/ Closed' if claim_no in claim_numbers_2022 else 'Still_Outstanding'

# Apply the function to each row of data_OS_2021
data_OS_2021['Status'] = data_OS_2021['ClaimNo'].apply(check_status)

# Calculate claim indicator count, total OS amount and percentage for 2021
claim_indicator_count_2021 = data_OS_2021.groupby('Claim Indicator').agg({'OS Amount': ['count', 'sum']})
claim_indicator_count_2021.columns = ['count', 'total_OS_Amount']
claim_indicator_count_2021['percentage'] = claim_indicator_count_2021['total_OS_Amount'] / claim_indicator_count_2021['total_OS_Amount'].sum() * 100

# Calculate claim indicator count, total OS amount and percentage for 2022
claim_indicator_count_2022 = data_OS_2022.groupby('Claim Indicator').agg({'OS Amount': ['count', 'sum']})
claim_indicator_count_2022.columns = ['count', 'total_OS_Amount']
claim_indicator_count_2022['percentage'] = claim_indicator_count_2022['count'] / claim_indicator_count_2022['count'].sum() * 100

# Calculate total OS amount summary by Class for 2022 where Claim Indicator is 'E1'
claim_indicator_sum_2022 = data_OS_2022[data_OS_2022['Claim Indicator'] == 'E1'].groupby('IRA Class')['OS Amount'].sum()

# Calculate count and total Gross Paid for Paid Claims in 2022
Paid_claims_indicator_count_sum_2022 = data_Paid_2022.groupby('Claim Indicator').agg({'Gross Paid': ['count', 'sum']})
Paid_claims_indicator_count_sum_2022.columns = ['count', 'total_Gross_Paid']

# Calculate count and total Gross Paid for Paid Claims in 2022 by Final Claim Indicator
Paid_Final_claims_indicator_count_sum_2022 = data_Paid_2022.groupby('Final Claim Indicator').agg({'Gross Paid': ['count', 'sum']})
Paid_Final_claims_indicator_count_sum_2022.columns = ['count', 'total_Gross_Paid']

# Calculate count and total Gross Paid for Paid Claims in 2022 by Loss Year where Revised Claim Indicator is 'B2'
Paid_claims_Loss_year_count_sum_2022 = data_Paid_2022[data_Paid_2022['Revised Claim Indicator'] == 'B2'].groupby('Loss Year')['Gross Paid'].agg(['count', 'sum'])

# Calculate total OS amount for OS claims by Loss Year for 2022
OS_claims_by_Loss_Year_2022 = data_OS_2022.groupby('Loss Year')['OS Amount'].sum()

# Calculate total OS amount for OS claims by Loss Year for 2023
OS_claims_by_Loss_Year_2023 = data_OS_2023.groupby('Loss Year')['OS Amount'].sum()

# Calculate total OS amount for OS Claims by IRA CLASS
OS_claims_by_IRA_Class = data_OS_2023.groupby('IRA Class')['OS Amount'].sum()

# Calculate total OS amount for OS Claims by IRA CLASS for 2023
OS_claims_by_IRA_Class_2023 = data_OS_2023[data_OS_2023['Loss Year'] == 2023].groupby('IRA Class')['OS Amount'].sum()