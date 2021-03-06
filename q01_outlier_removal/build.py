# %load q01_outlier_removal/build.py
# Default imports
import pandas as pd

loan_data = pd.read_csv('data/loan_prediction_uncleaned.csv')
loan_data = loan_data.drop('Loan_ID', 1)


# Write your Solution here:
def outlier_removal(df):
    df = df.drop(df[(df['ApplicantIncome']>df['ApplicantIncome'].quantile(0.95)) | 
                    (df['CoapplicantIncome']>df['CoapplicantIncome'].quantile(0.95)) | 
                    (df['LoanAmount']>df['LoanAmount'].quantile(0.95))].index)
    
    return df
   
# outlier_removal(loan_data)
# loan_data.head()


