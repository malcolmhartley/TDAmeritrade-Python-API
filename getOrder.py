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
    blah = '\n***MISSING ARGUMENT #1 (ORDER-ID)***\nC:\> python3 getOrder.py 2437370499\n'
print (blah)

# Grabbing Authorization code from file in local DIR
path = 'access_token'
access_token = open(path,'r')
code = access_token.read()
code = code.rstrip()
headers = {}
headers['Authorization'] = 'Bearer ' + code

# HTTP Request
orderId = sys.argv[1] #2437370499
response = requests.get('https://api.tdameritrade.com/v1/accounts/493539792/orders/{}'.format(orderId), headers=headers)

data = response.json()
output = json.dumps(data, indent=4)
#print (output)

file_name = r"order.csv"

leg_df = pd.io.json.json_normalize(data['orderLegCollection'])
leg_df.columns = leg_df.columns.map(lambda x: x.split(".")[-1])
#print (leg_df)

theRest_df = pd.DataFrame(data, columns=['orderStrategyType', 'orderId', 'cancelable', 'editable', 'status', 'enteredTime', 'accountId', 'session', 'duration', 'orderType', 'complexOrderStrategyType', 'quantity', 'filledQuantity', 'remainingQuantity', 'requestedDestination', 'destinationLinkName', 'price'], index=[0])
#print (theRest_df)

order_df = pd.concat([leg_df, theRest_df], axis=1, ignore_index=False)
print (order_df)

order_df.to_csv(file_name, header = True)
print("The Data has been successfully dumped to the CSV file.")
print("-"*80)
