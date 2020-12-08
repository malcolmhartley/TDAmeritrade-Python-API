import requests
import pandas as pd
import json
import csv
import ast
from pandas.io.json import json_normalize

# Grabbing Authorization code from file in local DIR
path = 'access_token'
access_token = open(path,'r')
code = access_token.read()
code = code.rstrip()
headers = {}
headers['Authorization'] = 'Bearer ' + code

# HTTP Request Parameters
params = (
          ('fields', 'positions,orders'),
          )

# HTTP Request
response = requests.get('https://api.tdameritrade.com/v1/accounts/493539792', headers=headers, params=params)

# data holds everything retrned in API Call
data = response.json()

# Current / Initial / Projected Account Balances
current_df = pd.DataFrame(data['securitiesAccount']['currentBalances'], index=['currentBalances'])
initial_df = pd.DataFrame(data['securitiesAccount']['initialBalances'], index=['initialBalances'])
project_df = pd.DataFrame(data['securitiesAccount']['projectedBalances'], index=['projectedBalances'])

# Combine all balances into one data frame
frames = [current_df, initial_df, project_df]
result = pd.concat(frames)

# define your file name.
file_name = r"account_balances.csv"

# this will flip the columns with the rows
result_transposed = result.transpose()

# dump the data to the CSV file.
result_transposed.to_csv(file_name, header = True)

# print the status to the user
print("The Data has been successfully dumped to the CSV file.")
print("-"*80)

# print it so you can see the results
print("Here is my data frame transposed.")
print("-"*80)
print (result_transposed)

# Re-name output file for position information
file_name = r"position_info.csv"

# Normalize nested JSON data and output to .csv
positions_df = pd.io.json.json_normalize(data['securitiesAccount']['positions'])
positions_df.columns = positions_df.columns.map(lambda x: x.split(".")[-1])
positions_df.to_csv(file_name, header = True)
print (positions_df)

# Uncomment print to see everything the API call returns
output = json.dumps(data, indent=4)
print (output)

# StackOverflow fix for position_df issue I had
# https://stackoverflow.com/questions/34341974/nested-json-to-pandas-dataframe-with-specific-format
