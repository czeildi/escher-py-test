import requests
from pprint import pprint

port = '9292'
path = '/validate_request_py_py'
url = 'http://localhost:' + port + path
headers = {'X-EMS-Date': 'tomorrow'}
response = requests.get(url, headers = headers)

print('response text body:')
print(response.text)

print('response status:')
print(response.status_code)

print('headers:')
pprint(dict(response.headers), width = 1)
