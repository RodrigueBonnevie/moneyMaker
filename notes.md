# General 
  * Have a list of symbols that you want to look at.


# Portfolio
  * Make a class
  * This one takes in a list of symbols that it will trade on. 
  * Make it have a fixed amount of money
  * And have member functions that calls other functions such as moving average and such
  * You can have a ranking function also that returns a ranking metric on all stocks that it can buy fr

## portfolio implementation
  * Start with something that only trades one stock
  * It will always go all in on that stock if it has a buy signal
  * Must develop some kind of way to mock time in this implementation
    * either I have a paramteter in read data that makes it read to a certain point in time 

  * get data will have a start date and an end date, and to make this work we have be able to compare dates since there are dates missing in 
  * the data due to non working days.

# Data visualization
## What do I want to visualize?
  * Equity curve
  * data on how many trades where done and some statistics on their success
    * Like a histogram on the win/loss on trades
    * And some easily accesable data on average trade win, average holding time and how many buysignals we had
  * Maybe some plots on where I generate buy signals and where I want to sell
  
### Trading visualization
  Would be nice to have some kind of subplot where you visualize the tree or so best stocks and the tree or so worst stocks
  What could be shown could be for example where the buy signals are generated and where sell signals are genreated could be nice to do this with colors on the graph

  * Todo: plots have been made for different stocks, what's left to do is to show the buy and sell signals, one simple way of doing it is to just make two plots that are masked with either signal