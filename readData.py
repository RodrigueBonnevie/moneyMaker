import numpy as np
import json
import datetime

def readData(symbol, dataToStr, dataFromStr="1900-01-01"):
    dataUntilSplit = dataToStr.split("-")
    dataTo = datetime.datetime(int(dataUntilSplit[0]),int(dataUntilSplit[1]),int(dataUntilSplit[2]))
    dataFromSplit = dataFromStr.split("-")
    dataFrom = datetime.datetime(int(dataFromSplit[0]),int(dataFromSplit[1]),int(dataFromSplit[2]))

    f = open("data/" + symbol + ".json", "r")
    dataString = f.read()

    data = json.loads(dataString) 

    openList = []
    highList = [] 
    lowList = [] 
    closeList = [] 
    volumeList = [] 

    for key in data['Time Series (Daily)']: # todo: does this read prices from old to new or vice versa?
        keySplit = key.split("-")
        keyDate = datetime.datetime(int(keySplit[0]),int(keySplit[1]),int(keySplit[2]))
        if  (keyDate >= dataFrom and keyDate <= dataTo): # A bit stupid but probably the easiest to implement
            openList.append(float(data['Time Series (Daily)'][key]['1. open']))
            highList.append(float(data['Time Series (Daily)'][key]['2. high']))
            lowList.append(float(data['Time Series (Daily)'][key]['3. low']))
            closeList.append(float(data['Time Series (Daily)'][key]['4. close']))
            volumeList.append(float(data['Time Series (Daily)'][key]['5. volume']))

    stockName = data['Meta Data']['2. Symbol']
    parsedData = {"stock": stockName, 
                  "open": np.array(openList),
                  "high": np.array(highList),
                  "low": np.array(lowList),
                  "close": np.array(closeList),
                  "volume": np.array(volumeList)}
    return parsedData

def main():
    data = readData("test", "2022-01-19", dataFromStr="2022-01-13")
    print(data)

if __name__ == "__main__":
    main()