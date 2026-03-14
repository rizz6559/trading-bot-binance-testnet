from binance.client import Client

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"

def get_client():
    client = Client(API_KEY, API_SECRET, testnet=True)
    return client
