
import requests

#from .get_token import access_token

access_token = "kFueisrqPO8x3hDamgaL6QvfB3fZ"

short_code = "174379"

api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
headers = {"Authorization": "Bearer %s" % access_token}
request = { "ShortCode": short_code,
    "ResponseType": "Canceled",
    "ConfirmationURL": "http://0b1a8005.ngrok.io/c2b/confirmation",
    "ValidationURL": "http://0b1a8005.ngrok.io/c2b/validation_url"}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)