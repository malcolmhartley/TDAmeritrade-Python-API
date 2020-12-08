import requests
import json
import csv
import ast
import sys
import pandas as pd
import argparse


# First argument is order to replace
orderId = sys.argv[1]

# File containing order to replace it with
orderFile = sys.argv[2]


# Same format that getOrders.py outputs
with open(sys.argv[2]) as csvfile: #'sample_order.csv'
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        assetType = row[2]
        instruction = row[1]
        duration = row[18]
        price = row[26]
        orderType = row[19]
        quantity = row[21]
        symbol = row[5]


stock_marketOrder = {
    "orderType": "MARKET",
    "session": "NORMAL",
    "duration": duration,
    "orderStrategyType": "SINGLE",
    "orderLegCollection": [
        {
            "instruction": instruction,
            "quantity": quantity,
            "instrument": {
            "symbol": symbol,
            "assetType": assetType
            }
        }
    ]
}

stock_limitOrder = {
    "orderType": "LIMIT",
    "session": "NORMAL",
    "price": price,
    "duration": duration,
    "orderStrategyType": "SINGLE",
    "orderLegCollection": [
        {
            "instruction": instruction,
            "quantity": quantity,
            "instrument": {
            "symbol": symbol,
            "assetType": assetType
            }
        }
    ]
}

option_single = {
    "complexOrderStrategyType": "NONE",
    "orderType": "LIMIT",
    "session": "NORMAL",
    "price": price,
    "duration": duration,
    "orderStrategyType": "SINGLE",
    "orderLegCollection": [
        {
            "instruction": instruction,
            "quantity": quantity,
            "instrument": {
            "symbol": symbol,
            "assetType": assetType
            }
        }
    ]
}


# Grabbing Authorization code from file in local DIR
path = 'access_token'
access_token = open(path,'r')
code = access_token.read()
code = code.rstrip()
headers = {}
headers['Authorization'] = 'Bearer ' + code
headers['Content-Type'] = 'application/json'
#print (headers)


if orderType=='LIMIT' and assetType=='EQUITY':
    print ("order Type is "+orderType)
    params = json.dumps(stock_limitOrder).encode('utf8')
elif orderType=='MARKET':
    print ('Order Type is (sigh) '+orderType)
    params = json.dumps(stock_markerOrder).encode('utf8')
elif assetType=='OPTION' and orderType=='LIMIT':
    print ('Asset Type is '+assetType)
    params = json.dumps(option_single).encode('utf8')


#params = json.dumps(stock_limitOrder).encode('utf8')
print (params)

# HTTP Post Request
request = requests.put('https://api.tdameritrade.com/v1/accounts/493539792/orders/{}'.format(orderId), headers=headers, data=params)
request.status_code
request.json()
# Returns Error but works fine

