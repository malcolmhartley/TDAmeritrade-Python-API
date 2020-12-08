from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import requests
import ssl

class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
    
    def do_GET(self):
        self._set_headers()
        #Get the Auth Code
        path, _, query_string = self.path.partition('?')
        code = parse_qs(query_string)['code'][0]
        #code = input("Copy/Paste code here:\n")
        print(code)
        
        #Post Access Token Request
        headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
        data = { 'grant_type': 'authorization_code', 'access_type': 'offline', 'code': code, 'client_id': 'HARTLEYCAP1', 'redirect_uri': 'https://127.0.0.1'}
        authReply = requests.post('https://api.tdameritrade.com/v1/oauth2/token', headers=headers, data=data)
        
        #returned just to test that it's working
        self.wfile.write(authReply.text.encode())
        raw = authReply.json()
        print ("\n\n*** WROTE ACCESS/REFRESH TOKEN TO FILE ***\n\n")
        access_token = raw['access_token']
        refresh_token = raw['refresh_token']
        
        access_token_path = 'access_token'
        refresh_token_path = 'refresh_token'
        access_token_file = open('access_token','w')
        refresh_token_file= open('refresh_token','w')
        access_token_file.write(access_token)
        refresh_token_file.write(refresh_token)


httpd = HTTPServer(('127.0.0.1', 443), Handler)

#SSL cert
httpd.socket = ssl.wrap_socket (httpd.socket,
                                keyfile='SSL/key.pem',
                                certfile='SSL/certificate.pem', server_side=True)

#PAUL CHANGE "HARTLEYCAP1" and your redirect URL if needed
print ("POINT BROWSER TO: https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=https://127.0.0.1&client_id=HARTLEYCAP1%40AMER.OAUTHAP")
httpd.serve_forever()
