#!/usr/bin/python
import csv
import statistics

class Stock:
    def __init__(self, symbol):
        self.symbol = str(symbol)
        self.symbolBought = 0
        self.symbolSold = 0
        self.symbolPosition = self.symbolBought - self.symbolSold
        self.trades = 0 # counts total number of trades for this stock

    def buy(self, sharesBought):
        self.trades +=1
        sharesBought = int(sharesBought) # should trigger error if not an int but there's a check below
        if type(sharesBought) is not int:
            raise TypeError("Please enter integer value of shares to buy")
        self.symbolBought += sharesBought
        self.updatePosition()

    def sell(self, sharesSold):
        self.trades += 1
        sharesSold = int(sharesSold)
        if type(sharesSold) is not int:
            raise TypeError("Please enter integer value of shares to sell")
        self.symbolSold += sharesSold
        self.updatePosition()

    def updatePosition(self): # function to update symbolPosition
        self.symbolPosition = self.symbolBought - self.symbolSold

class Exchange:
    def __init__(self, name):
        self.name = name
        self.totalBought = 0
        self.totalSold = 0
        self.totalBoughtNotional = 0
        self.totalSoldNotional = 0

    def buy(self, shares, value):
        if type(shares) is not int:
            raise TypeError("Enter integer value")
        self.totalBought += shares
        self.totalBoughtNotional += value

    def sell(self, shares, value):
        if type(shares) is not int:
            raise TypeError("Enter integer value")
        self.totalSold += shares
        self.totalSoldNotional += value

def main(file):
    with open(file,'r+') as f:
        log = f.readlines() # reads lines as a list of (mostly) trades
        f.close()
    stockData = {} # keeps stock data
    exchangeData = {} # keeps exchange data
    totalTrades = 0
    totalBought = 0
    totalSold = 0
    buyTradeValues = []
    sellTradeValues = []
    output = [log[0]]
    log = log[1:]  # skips header line since it isn't a trade, it's titles

    for line in log:
        line = line.split(',')
        output.append(line[0]+','+line[1]+','+line[2]+','+line[3]+','+line[4]+','+line[5]+','+line[6]+','+line[7]+','+line[8]+','+line[9]+','+line[10]+','+line[11]+','+line[12]+','+line[13]+','+line[14]+','+line[15]+','+line[16]+'\n')
        if line[2] == 'TRADE': # makes sure current line is a trade
            totalTrades += 1 # keeps track of total number of trades
            if line[1] not in stockData: # creates stock if it doesn't exist
                s = Stock(line[1])
                stockData[line[1]]= s
            else:
                s = stockData[line[1]] # gets stock from dict if it exists

            if line[6] not in exchangeData: # creates exchange if it doesn't exist
                e = Exchange(line[6])
                exchangeData[line[6]] = e
            else:
                e = exchangeData[line[6]] # gets exchange data if it exists

            q = int(line[4]) # quantity of shares in the trade
            v = int(line[10]) # value of shares
            if line[3] == 'b': # buy
                s.buy(q) # updates stock buy
                e.buy(q,v) # updates exchange buy
                totalBought += q # updates total bought
                buyTradeValues.append(v)

            elif line[3] == 't' or line[3] == 's':
                s.sell(q) # updates stock sold
                e.sell(q,v) # updates exchange sold
                totalSold += q # updates total sold
                sellTradeValues.append(v)

            else:
                raise Exception("Trades accepted are 'b', 's', or 't'")


    # Output

    print('Processed Trades: ' + str(totalTrades))
    print('Shares Bought: ' + str(totalBought))
    print('Total Sold: ' + str(totalSold))
    print('Total Volume: ' + str(totalBought + totalSold))
    print('Notional Bought: ' + '${:0,.2f}'.format(sum(buyTradeValues)))
    print('Notional Sold: ' + '${:0,.2f}'.format(sum(sellTradeValues)))
    print()
    print('Per Exchange Volumes: ')

    for trade in exchangeData.keys():
        e = exchangeData[trade]
        exchange = e.name
        b = e.totalBought
        s = e.totalSold
        print(str(exchange) + ' Bought: ' + str(b) + ' shares')
        print(str(exchange) + ' Sold: ' + str(s) + ' shares')
    totalValue = buyTradeValues + sellTradeValues

    print()
    print('Average Trade Size: ' + '${:0,.2f}'.format(statistics.mean(totalValue)))
    print('Median Trade Size: ' + '${:0,.2F}'.format(statistics.median(totalValue)))
    print()
    print('Stocks that moved the most:')
    def getNumberOfSales(stock): # key for sorting sales
        return stock.symbolBought + stock.symbolSold

    s = list(stockData.values())
    s = sorted(s, key=getNumberOfSales) # sorts stock data so we can get top 10 stocks
    s.reverse()
    for i in range(10):
        print(str(i+1) + ' - ' + s[i].symbol + ': ' + str(s[i].symbolBought + s[i].symbolSold) + ' shares moved')

    with open ('tradesOutput.csv', 'w+') as f:
        for line in output:
            f.write(line)
        f.close()



if __name__ == '__main__':
    main('EnrichedTrades.csv')