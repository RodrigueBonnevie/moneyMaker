from readData import readData
from movinAverage import buyMovingAverage
import datetime

class portfolioManager:
    def __init__(self, money, stockSymbols):
        ''' stocks should be a list with all stock sybols that we want to monitor'''
        self.stockSymbols = stockSymbols
        self.date = datetime.datetime.now()
        self.buyStatus = {}
        self.ownedStocks = {}
        self.liquidCapital = money  # Money available to the bot
        for stockSymbol in stockSymbols:
            self.buyStatus[stockSymbol] = False


    def buyNsell(self, date): # should this just take in one stock and then evaluate just do the buying or selling?
        for stockSymbol in self.buyStatus:
            if (self.buyStatus[stockSymbol]): 
                if self.liquidCapital > 0:
                    self.ownedStocks[stockSymbol] = self.liquidCapital / readData(stockSymbol, date)['close'][0]
                    self.liquidCapital = 0
            else:
                if stockSymbol in self.ownedStocks: # sell
                    self.liquidCapital += self.ownedStocks[stockSymbol] * readData(stockSymbol, date)['close'][0]
                    self.ownedStocks.pop(stockSymbol)

    def getCapital(self, date):
        capital = self.liquidCapital
        for stockSymbol in self.ownedStocks:
            capital += self.ownedStocks[stockSymbol] * readData(stockSymbol, date)['close'][0]
        return capital



# should I have a evaluate stocks that generates a by or sell signal for each stock
# then have a ranking function that ranks the potential buyable stocks can be in the order of the dict for now, fix this later
# do I really have to have everything in a class? isn't it better to have functions for most of the stuff and more like a struch for the portfolio?
# then you could create multiple portfolios and just make them buy and trade with different functions  

def main():
    date =  "2021-03-31"
    longMA = 200
    shortMA = 50
    stockSymbols = ['AAPL', 'IBM']
    bot = portfolioManager(10000, stockSymbols)
    bot.buyStatus = buyMovingAverage(bot.stockSymbols, date, longMA, shortMA) 
    bot.buyNsell(date)
    print("but status: ", bot.buyStatus)
    print("owned stocks: ", bot.ownedStocks)
    print("liquid capital", bot.liquidCapital)
    print("capital", bot.getCapital(date))
    bot.buyStatus["AAPL"] = False
    bot.buyNsell(date)
    print("buy status: ", bot.buyStatus)
    print("owned stocks: ", bot.ownedStocks)
    print("liquid capital", bot.liquidCapital)
    print("capital", bot.getCapital(date))

if __name__ == "__main__":
    main()