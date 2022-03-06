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
    while (date < endDate):
        dateStr = date.strftime("%Y-%m-%d")
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

def plotBuyStatus(evaluationData, startDate, endDate):
    plt.figure()

    plt.subplot(1,2,1)
    applData = readData("AAPL", endDate, dataFromStr=startDate)
    plt.plot(np.arange(0,applData["close"].size),np.flip(applData["close"]))
    plt.title("AAPL")
    plt.xlabel('Days running')
    plt.ylabel('Stock value')

    plt.subplot(1,2,2)
    applData = readData("IBM", endDate, dataFromStr=startDate)
    plt.plot(np.arange(0,applData["close"].size),np.flip(applData["close"]))
    plt.title("IBM")
    plt.xlabel('Days running')
    plt.ylabel('Stock value')

    print("Buy signal per stock")
    print(evaluationData.buySignalPerStock)



def main():
    startDate =  "2021-03-30"
    endDate =  "2021-04-10"
    longMA = 3
    shortMA = 2
    stockSymbols = ['AAPL', 'IBM']
    bot = portfolioManager(10000, stockSymbols)
    evaluationData = runBackTest(startDate, endDate, bot, longMA, shortMA)

    #plot(evaluationData.equity)
    plotEquity(evaluationData)
    plotBuyStatus(evaluationData, startDate, endDate)




if __name__ == "__main__":
    main()
    plt.show()