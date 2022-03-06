import numpy as np
import matplotlib.pyplot as plt

from portfolioManager import* 

def runBackTest(startDateStr, endDateStr, bot, longMA, shortMA):
    dateSplit = startDateStr.split("-")
    startDate = datetime.datetime(int(dateSplit[0]),int(dateSplit[1]),int(dateSplit[2]))
    dateSplit = endDateStr.split("-")
    endDate = datetime.datetime(int(dateSplit[0]),int(dateSplit[1]),int(dateSplit[2]))
    capital = np.array([])

    date = startDate
    while (date < endDate):
        dateStr = date.strftime("%Y-%m-%d")
        bot.buyStatus = buyMovingAverage(bot.stockSymbols, dateStr, longMA, shortMA) 
        bot.buyNsell(dateStr)
        capital = np.append(capital, bot.getCapital(dateStr))
        date += datetime.timedelta(days=1)
    return capital

def plot(data):
    plt.figure()
    plt.plot(data)
    

def main():
    startDate =  "2021-03-30"
    endDate =  "2021-05-10"
    longMA = 200
    shortMA = 50
    stockSymbols = ['AAPL', 'IBM']
    bot = portfolioManager(10000, stockSymbols)
    capital = runBackTest(startDate, endDate, bot, longMA, shortMA)

    plot(capital)




if __name__ == "__main__":
    main()
    plt.show()