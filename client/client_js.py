import requests
from pprint import pprint
from escherauth_go.escher_signer import EscherSigner

port = '8080'
path = '/validate_request_py_js'
host = 'http://localhost:' + port
url = host + path

def escherSignedHeader(host, path):
    signer = EscherSigner(
      'EscherPyExample',
      'ildiescherpysecret',
      'example/credential/scope'
    )
    signed_headers = signer.signRequest(
        method='GET', url=path, body='', headers={'Host': host})
    return signed_headers

signed_headers = escherSignedHeader(
  host=host, path=path#, extra_headers={'Content-Type': 'application/json'}
)
response = requests.get(url, headers=signed_headers)

print('response text body:')
print(response.text)

print('response status:')
print(response.status_code)

print('headers:')
pprint(dict(response.headers), width=1)

