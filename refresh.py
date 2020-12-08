from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import requests
import ssl

import time
starttime=time.time()
while True:

    # Naming File Pointers
    refresh = 'refresh_token'
    access = 'access_token'

    # Opening Refresh-token file
    refresh_token_file = open(refresh,'r')

    # Reading Refresh-Token from file, then closing FP.
    refresh_token = refresh_token_file.read()
    refresh_token_file.close()

    #print ("Old Refresh\n" + refresh_token)

    #Post Refresh Token Request
    headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
    data = { 'grant_type': 'refresh_token', 'refresh_token': refresh_token, 'access_type': 'offline', 'code': '', 'client_id': 'HARTLEYCAP1', 'redirect_uri': ''}
    authReply = requests.post('https://api.tdameritrade.com/v1/oauth2/token', headers=headers, data=data)

    raw = authReply.json()
    print ("\n*** WROTE NEW TOKENS TO FILE ***\n")

    # New Values to Tokens
    access_token = raw['access_token']
    refresh_token = raw['refresh_token']

    # Re-opening Access/Refresh token files for writing
    access_token_file = open(access, 'w')
    refresh_token_file = open(refresh,'w')

    # Writing new Access/Refresh Token Values
    access_token_file.write(access_token)
    refresh_token_file.write(refresh_token)

    # Closing files again to be safe
    access_token_file.close()
    refresh_token_file.close()

    # Repeat the process again in before 30 minute timeout mark
    print ('*** 30 Mins Passed ***')
    time.sleep(1740.0 - ((time.time() - starttime) % 1740.0))
