import requests
def get_crypto_price(symbol):
    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': symbol.upper(),
        'convert': 'USD'  # You can change this to convert to other currencies
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'a9369a4d-1231-4827-a774-93a18e73caec',  # Replace with your API key
    }

    try:
        response = requests.get(url, params=parameters, headers=headers)
        data = response.json()
        if 'data' in data and symbol.upper() in data['data']:
            price = data['data'][symbol.upper()]['quote']['USD']['price']
            return price
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

# other info
    
import requests
import json

def get_crypto_info(symbol):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
    parameters = {
        'symbol': symbol
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'a9369a4d-1231-4827-a774-93a18e73caec',  # Replace with your API key
    }

    session = requests.Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


