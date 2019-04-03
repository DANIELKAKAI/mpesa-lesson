import requests
from requests.auth import HTTPBasicAuth

consumer_key = "BmJA23hoT8h7QTH0FwmvfIrJDiu7ADPY"
consumer_secret = "HzMA4GqNIVITRoKR"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

access_token = r.json()['access_token']



if __name__=='__main__':
	pass