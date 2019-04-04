import requests



access_token = "kFueisrqPO8x3hDamgaL6QvfB3fZ"

short_code = "174379"


api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
headers = {"Authorization": "Bearer %s" % access_token}
request = { "ShortCode":short_code,
  "CommandID":"CustomerPayBillOnline",
  "Amount":"5",
  "Msisdn":"254708374149",
  "BillRefNumber":"learning" }

response = requests.post(api_url, json = request, headers=headers)

print (response.text)