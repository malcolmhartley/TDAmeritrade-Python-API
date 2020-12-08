import requests
import json
import csv
import pandas as pd
import ast
from pandas.io.json import json_normalize
import sys

# Capturing First Command Line Arg as OrderId
if len(sys.argv) > 1:
    blah = sys.argv[1]
else:
    blah = '\n*** MISSING ARGUMENT #1 (TRANSACTION_ID) ***\nC:\> python3 getTransaction.py 24374023073\n'
print (blah)

# Grabbing Authorization code from file in local DIR
path = 'access_token'
access_token = open(path,'r')
code = access_token.read()
code = code.rstrip()
headers = {}
headers['Authorization'] = 'Bearer ' + code

# HTTP Request
transactionId = sys.argv[1] #2437370499
response = requests.get('https://api.tdameritrade.com/v1/accounts/493539792/transactions/{}'.format(transactionId), headers=headers)

data = response.json()
output = json.dumps(data, indent=4)
print (output)

file_name = r"transaction.csv"

transaction_df = pd.io.json.json_normalize(data)
transaction_df.columns = transaction_df.columns.map(lambda x: x.split(".")[-1])
transaction_df.to_csv(file_name, header = True)
#print (transactions_df)
print("The Data has been successfully dumped to the CSV file.")
print("-"*80)
print (transaction_df)
