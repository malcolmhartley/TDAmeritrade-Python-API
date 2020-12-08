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
    blah = '\n*** MISSING ARGUMENT #1 (ORDER-ID) ***\nC:\> python3 cancelOrder.py 2437370499\n'
print (blah)

# Grabbing Authorization code from file in local DIR
path = 'access_token'
access_token = open(path,'r')
code = access_token.read()
code = code.rstrip()
headers = {}
headers['Authorization'] = 'Bearer ' + code

# HTTP Delete Request
orderId = sys.argv[1] #2437370499
response = requests.delete('https://api.tdameritrade.com/v1/accounts/493539792/orders/{}'.format(orderId), headers=headers)

print("Order successfully removed from Queue")
print("-"*80)
