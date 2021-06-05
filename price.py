import requests

def btcbrl():
  url = 'https://blockchain.info/tobtc?currency=BRL&value=1'

  result = requests.get(url)

  result = 1/result.json()

  result = str(f"{result:.2f}")
  
  return result

def ethbrl():
  url = 'https://api.bitpreco.com/eth-brl/ticker'

  result = requests.get(url)

  return str(f"{result.json()['buy']:.2f}")