import requests
import json
import csv
import pandas as pd

# Grabbing Authorization code from file in local DIR
path = 'access_token'
access_token = open(path,'r')
code = access_token.read()
code = code.rstrip()
headers = {}
headers['Authorization'] = 'Bearer ' + code

# HTTP Request
response = requests.get('https://api.tdameritrade.com/v1/accounts/493539792/transactions?type=ALL', headers=headers)

data = response.json()
output = json.dumps(data, indent=4)
#print (output)

file_name = r"transactions.csv"

transactions_df = pd.io.json.json_normalize(data)
transactions_df.columns = transactions_df.columns.map(lambda x: x.split(".")[-1])
transactions_df.to_csv(file_name, header = True)
#print (transactions_df)
print("The Data has been successfully dumped to the CSV file.")
print("-"*80)
print (transactions_df)
