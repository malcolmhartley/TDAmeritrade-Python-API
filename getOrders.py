import requests
import json
import csv
import pandas as pd
import ast
from pandas.io.json import json_normalize


# Grabbing Authorization code from file in local DIR
path = 'access_token'
access_token = open(path,'r')
code = access_token.read()
code = code.rstrip()
headers = {}
headers['Authorization'] = 'Bearer ' + code

# HTTP Request
response = requests.get('https://api.tdameritrade.com/v1/accounts/493539792/orders', headers=headers)

data = response.json()
output = json.dumps(data, indent=4)
#print (output)

file_name = r"orders.csv"

#one_df = pd.DataFrame(data, columns=['session', 'duration', 'orderType', 'complexOrderStrategyType', 'quantity', 'filledQuantity', 'remainingQuantity', 'requestedDestination', 'destinationLinkName', 'price'])
#print (one_df)
#one_df.to_csv(file_name, header = True)

#two_df = pd.io.json.json_normalize(data[0]['orderLegCollection'])
#two_df.columns = two_df.columns.map(lambda x: x.split(".")[-1])
#print (two_df)
#two_df.to_csv(file_name, header = True)

#print (test_df)

test_df = pd.DataFrame()
for item in data:
    test_df = test_df.append(json_normalize(item['orderLegCollection']))
#print (item['orderLegCollection'])

test_df.reset_index(drop=True, inplace=True)
#print (test_df)

#test_df.to_csv(file_name, header = True)

#three_df = pd.DataFrame(data, columns=['orderStrategyType', 'orderId', 'cancelable', 'editable', 'status', 'enteredTime', 'accountId'])
one_df = pd.DataFrame(data, columns=['orderStrategyType', 'orderId', 'cancelable', 'editable', 'status', 'enteredTime', 'accountId', 'session', 'duration', 'orderType', 'complexOrderStrategyType', 'quantity', 'filledQuantity', 'remainingQuantity', 'requestedDestination', 'destinationLinkName', 'price'])
#print (one_df)

#frames = [one_df, three_df]
#concat_df = pd.concat(frames, sort=False)
#print (concat_df)

# Combine all balances into one data frame
#frames = [one_df, test_df]
#orders_df = pd.concat(frames)

#print (one_df)

#one_df.merge(test_df)
#orders_df = pd.merge(one_df, test_df, how='left')
orders_df = pd.concat([test_df, one_df], axis=1, ignore_index=False)
print (orders_df)

orders_df.to_csv(file_name, header = True)
              
#orders_df_transposed = orders_df.transpose()
#orders_df_transposed.to_csv(file_name, header = True)

#orders_df = pd.DataFrame(data['orderLegCollection'])
#print (orders_df)

print("The Data has been successfully dumped to the CSV file.")
print("-"*80)
#print (orders_df_transposed)
