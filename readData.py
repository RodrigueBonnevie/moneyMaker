import numpy as np
import json
import datetime

def readData(symbol, dataUntilStr):
    dataUntilSplit = dataUntilStr.split("-")
    dataUntil = datetime.datetime(int(dataUntilSplit[0]),int(dataUntilSplit[1]),int(dataUntilSplit[2]))

    f = open("data/" + symbol + ".json", "r")
    dataString = f.read()

    data = json.loads(dataString) 

    openList = []
    high = [] 
    low = [] 
    close = [] 
    volume = [] 
    dateee = "2022-01-02"

    for key in data['Time Series (Daily)']: # todo: does this read prices from old to new or vice versa?
        keySplit = key.split("-")
        keyDate = datetime.datetime(int(keySplit[0]),int(keySplit[1]),int(keySplit[2]))
        if  dataUntil < keyDate: # A bit stupid but probably the easiest to implement
            continue
        openList.append(float(data['Time Series (Daily)'][key]['1. open']))
        high.append(float(data['Time Series (Daily)'][key]['2. high']))
        low.append(float(data['Time Series (Daily)'][key]['3. low']))
        close.append(float(data['Time Series (Daily)'][key]['4. close']))
        volume.append(float(data['Time Series (Daily)'][key]['5. volume']))

    stockName = data['Meta Data']['2. Symbol']
    parsedData = {"stock": stockName, 
                  "open": np.array(openList),
                  "high": np.array(high),
                  "low": np.array(low),
                  "close": np.array(close),
                  "volume": np.array(volume)}
    return parsedData

def main():
  data = readData("IBM", "1999-11-03")
  print(data)
if __name__ == "__main__":
    main()