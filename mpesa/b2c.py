import requests
from .get_token import access_token
import datetime
import base64

api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer %s" % access_token }
passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
short_code = "174379"


def transaction(PhoneNumber,name):
  timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
  p = short_code+passkey+timestamp
  password = base64.b64encode(p.encode(), altchars=None).decode()
  request = {
    "BusinessShortCode": "174379",
    "Password": password,
    "Timestamp": timestamp,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "5",
    "PartyA": PhoneNumber,
    "PartyB": "174379",
    "PhoneNumber": PhoneNumber,
    "CallBackURL": "http://0b97724b.ngrok.io/mpesa-callback/",
    "AccountReference": name,
    "TransactionDesc": "testing mpesa"
  }
  response = requests.post(api_url, json = request, headers=headers)
  print (response.text)
  return response.text



if __name__=='__main__':
  pass