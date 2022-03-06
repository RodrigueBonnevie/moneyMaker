import json
import requests

symbol = "SPY"
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + symbol + '&outputsize=full&apikey=4I110AW02OO16XRG'
r = requests.get(url)
data = r.json()

stockName = data['Meta Data']['2. Symbol']

with open('data/'+ stockName +'.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

print("Retrieved and saved data from " + stockName)