import numpy as np
import matplotlib.pyplot as plt

from readData import readData



def buyMovingAverage(stockSymbols, date, longMA, shortMA):
    buyStatus = {}
    for stockSymbol in stockSymbols:
        stockData = readData(stockSymbol, date)
        longMean = np.mean(stockData["open"][-longMA:])
        shortMean = np.mean(stockData["open"][-shortMA:])
        buy = shortMean > longMean
        buyStatus[stockSymbol] = buy
    return buyStatus

def main():
    longMA = 200
    shortMA = 50
    buy = []
    index = 1
    #arr = np.arange(0,20)
    #print("range", arr)
    #data["open"] = arr
    for day in data["open"]:
      #print(index)
      if(index >= longMA):
          buy.append(buyMovingAverage(data["open"][index-longMA:index], longMA, shortMA))
          #print(data["open"][index-longMA:index])
          #print(buy)
      else:
          buy.append(False)
      index +=1


    #data = readData("IBM.json", "2020-01-01")
    #buyNp = np.array(buy)
    #stockMasked = np.multiply(buyNp, data["open"])
    #
    #xaxis = np.arange(0, data["open"].size)
    #plt.figure(1)
    #plt.plot(xaxis, data["open"])
    #plt.figure(2)
    #plt.plot(stockMasked)
    #
    #plt.show()
if __name__ == "__main__":
    main()