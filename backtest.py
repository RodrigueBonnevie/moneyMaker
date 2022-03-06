import numpy as np
import matplotlib.pyplot as plt

from portfolioManager import* 
class EvaluationData:
    #buySignalPerStock = {}  # dictionary with keys that are the stocksymbols and contains arrays of buy bools

    def __init__(self, bot):
        self.equity = np.array([])
        self.dates = []
        self.buySignalPerStock = {stockSymbol: [] for stockSymbol in bot.buyStatus}
        print(self.buySignalPerStock)

    def appendBuyStatus(self, buyStatus):
        for stockSymbol in buyStatus:
            self.buySignalPerStock[stockSymbol].append(buyStatus[stockSymbol])


def runBackTest(startDateStr, endDateStr, bot, longMA, shortMA):
    dateSplit = startDateStr.split("-")
    startDate = datetime.datetime(int(dateSplit[0]),int(dateSplit[1]),int(dateSplit[2]))
    dateSplit = endDateStr.split("-")
    endDate = datetime.datetime(int(dateSplit[0]),int(dateSplit[1]),int(dateSplit[2]))

    evaluationData = EvaluationData(bot)

    date = startDate
    while (date <= endDate):
        dateStr = date.strftime("%Y-%m-%d")
        stockMarketOpen = readData("AAPL", dateStr, dataFromStr=dateStr) # stockmarket are closed on weekends and stuff
        if (stockMarketOpen["open"].size != 0):
            print("Evaluating stocks on date " + dateStr)
            bot.buyStatus = buyMovingAverage(bot.stockSymbols, dateStr, longMA, shortMA) 
            bot.buyNsell(dateStr)

            # Save data for data visualization
            evaluationData.equity = np.append(evaluationData.equity, bot.getCapital(dateStr))
            evaluationData.dates.append(date)
            evaluationData.appendBuyStatus(bot.buyStatus)

        date += datetime.timedelta(days=1)
    return evaluationData

def plot(data):
    plt.figure()
    plt.plot(data)
    
def plotEquity(evaluationData):
    plt.figure()
    plt.plot(np.arange(0,evaluationData.equity.size),evaluationData.equity)
    plt.title('Equity curve')
    plt.xlabel('Days running')
    plt.ylabel('Money')

def maskBuyNSellOnStockData(stockSymbol, evaluationData, startDate, endDate):
    applData = readData(stockSymbol, endDate, dataFromStr=startDate)
    #buyPeriod = np.multiply(applData["close"], evaluationData.buySignalPerStock["AAPL"])
    buyMask = [not elem for elem in evaluationData.buySignalPerStock[stockSymbol]]
    buyPeriod = np.ma.masked_where(buyMask, np.flip(applData["close"])) # funny enough the mask has to be inverted since true values are masked in numpy
    sellPeriod = np.ma.masked_where(evaluationData.buySignalPerStock[stockSymbol], np.flip(applData["close"]))
    return {"buy":buyPeriod, "sell":sellPeriod}

def plotBuyStatus(evaluationData, startDate, endDate):
    plt.figure()

    plt.subplot(1,2,1)
    maskedStockData = maskBuyNSellOnStockData("AAPL", evaluationData, startDate, endDate)
    plt.plot(np.arange(0,maskedStockData["buy"].size),maskedStockData["buy"], label="buy")
    plt.plot(np.arange(0,maskedStockData["sell"].size),maskedStockData["sell"], label="sell")
    plt.title("AAPL")
    plt.xlabel('Days running')
    plt.ylabel('Stock value')
    plt.legend()

    plt.subplot(1,2,2)
    maskedStockData = maskBuyNSellOnStockData("IBM", evaluationData, startDate, endDate)
    plt.plot(np.arange(0,maskedStockData["buy"].size),maskedStockData["buy"], label="buy")
    plt.plot(np.arange(0,maskedStockData["sell"].size),maskedStockData["sell"], label="sell")
    plt.title("IBM")
    plt.xlabel('Days running')
    plt.ylabel('Stock value')
    plt.legend()





def main():
    startDate =  "2021-02-06"
    endDate =  "2021-05-10"
    longMA = 15
    shortMA = 5
    stockSymbols = ['AAPL', 'IBM']
    bot = portfolioManager(10000, stockSymbols)
    evaluationData = runBackTest(startDate, endDate, bot, longMA, shortMA)

    #plot(evaluationData.equity)
    plotEquity(evaluationData)
    plotBuyStatus(evaluationData, startDate, endDate)




if __name__ == "__main__":
    main()
    plt.show()