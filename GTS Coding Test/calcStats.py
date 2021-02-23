#!/usr/bin/python

import sys
import csv
from tempfile import NamedTemporaryFile
import shutil
import statistics

class Stock:
    def __init__(self,symbol):
        self.symbol = str(symbol)
        self.symbolBought = 0
        self.symbolSold = 0
        self.symbolPosition = self.symbolBought - self.symbolSold # Symbol Position is difference between symbol Bought/Sold

    def buy(self, shares):
        if type(shares) is not int:
            raise TypeError('Please buy an integer number of shares')
        self.symbolBought += shares
        self.updatePosition()

    def sell(self, shares):
        if type(shares) is not int:
            raise TypeError('Please sell an integer number of shares')
        self.symbolSold += shares
        self.updatePosition()

    def updatePosition(self): # checks symbolPosition after a transaction
        self.symbolPosition = self.symbolBought - self.symbolSold

class Exchange: # keep track of stocks bought/sold on each exchange
    def __init__(self,name):
        self.exchangeName = str(name)
        self.exchangeBought = 0
        self.exchangeSold = 0

    def buy(self, shares):
        if type(shares) is not int:
            raise TypeError('Please buy an integer number of shares')
        self.exchangeBought += shares

    def sell(self, shares):
        if type(shares) is not int:
            raise TypeError('Please sell an integer number of shares')
        self.exchangeSold += shares

def main():
    # create variables for input and output files so they can be easily changed
    inputFile = str(input('Please input a file name to analyze: '))
    outputFile = NamedTemporaryFile('w', delete=False) # can't edit in place effectively, so write to temp file as we go

    with open(inputFile) as csvFile:
        reader = csv.reader(csvFile, delimiter=',') # file to read data from
        writer = csv.writer(outputFile, delimiter=',') # write to temp file since we can't write to input file without risking miswriting CSV

        symbolsUsed = [] # makes it easier to tell if we already have data for this stock
        exchangesUsed = [] # keeps track of exchanges we already have data for
        stockData = []
        exchangeData = []

        totalBought = []
        totalSold = []
        totalBoughtNotional = []
        totalSoldNotional = []
        totalSharesTraded = []
        for row in reader: # each row is a trade
            if row[2] == 'TRADE': # ignores title and makes sure EventType is actually a trade

                if row[3] not in ['b','s','t']: # makes sure side is a valid buy or sell
                    raise ValueError('Side should be b,s, or t to indicate a buy, sell, or short')
                if row[3] == 'b':
                    tradeType = 'BUY'
                else:
                    tradeType = 'SELL'

                shareCount = int(row[4]) # number of shares in this transaction (as int so it can be added)
                totalSharesTraded.append(shareCount)

                if row[1] not in symbolsUsed: # makes sure we have a variable for stock data
                    symbolsUsed.append(row[1]) # adds the symbol to list of used symbols
                    stockData.append(Stock(row[1]))
                for stock in stockData:
                    if stock.symbol == row[1]:
                        if tradeType == 'BUY': # counts buys of stock with number from FillSize
                            stock.buy(shareCount)
                        else: # counts sells of stock with number from FillSize
                            stock.sell(shareCount)
                        symbolNotional = int(shareCount * float(row[5])) # multiplies FillSize * FillPrice, rounded to 2 decimals
                        # add stock data to row
                        try: #
                            row += [stock.symbolBought, stock.symbolSold, stock.symbolPosition, symbolNotional]
                        except:
                            raise Exception('Stock data failed to add to row')

                if row[6] not in exchangesUsed: # makes sure we have a variable for exchange data
                    exchangesUsed.append(row[6])
                    exchangeData.append(Exchange(row[6]))
                for exchange in exchangeData:
                    if exchange.exchangeName == row[6]:
                        if tradeType == 'BUY': # counts shares bought from exchange with num from FullSize
                            exchange.buy(shareCount)
                        else: # counts shares sold from exchange
                            exchange.sell(shareCount)
                    # add exchange data to row
                        try:
                            row += [exchange.exchangeBought, exchange.exchangeSold]
                        except:
                            raise Exception('Exchange data failed to add to row')

                if tradeType == 'BUY': # update buy values
                    if len(totalBought) != 0: # if there is a value in totalBought, add to prev
                        totalBought.append(totalBought[-1] + shareCount)
                        totalBoughtNotional.append(totalBoughtNotional[-1] + symbolNotional)
                        totalSold.append(totalSold[-1])
                        totalSoldNotional.append(totalSoldNotional[-1])
                    else: # if it is the first row, just insert values
                        totalBought.append(shareCount)
                        totalBoughtNotional.append(symbolNotional)
                        totalSold.append(0)
                        totalSoldNotional.append(0)
                else: # update sell values
                    if len(totalSold) != 0:
                        totalSold.append(totalSold[-1] + shareCount)
                        totalSoldNotional.append((totalSoldNotional[-1]) + symbolNotional)
                        totalBought.append(totalBought[-1])
                        totalBoughtNotional.append(totalBoughtNotional[-1])
                    else:
                        totalSold.append(shareCount)
                        totalSoldNotional.append(symbolNotional)
                        totalBought.append(0)
                        totalBoughtNotional.append(0)
                try:
                    row += [totalBought[-1], totalSold[-1], totalBoughtNotional[-1], totalSoldNotional[-1]]
                except:
                    raise Exception('Could not add total values')

            # Write output data
            if row[2] != 'TRADE': # writes first row with titles
                title = row + ['SymbolBought','SymbolSold','SymbolPosition','SymbolNotional','ExchangeBought','ExchangeSold','TotalBought','TotalSold','TotalBoughtNotional','TotalSoldNotional']
                writer.writerow(title)
            else: # write trade rows
                writer.writerow(row)
        outputFile.close()
        shutil.move(outputFile.name,'EnrichedTrades.csv')

        print('Processed Trades:', len(totalBought))
        print('')
        print('Shares Bought:', totalBought[-1])
        print('Shares Sold:', totalSold[-1])
        print('Total Volume:', totalBought[-1] + totalSold[-1])
        print('Notional Bought:', '${:0,.2f}'.format(totalBoughtNotional[-1]))
        print('Notional Sold:', '${:0,.2f}'.format(totalSoldNotional[-1]))
        print('')
        print('Per Exchange Volumes:')
        for exchange in exchangeData:
            print(exchange.exchangeName, ' Bought:', exchange.exchangeBought)
            print(exchange.exchangeName, 'Sold:', exchange.exchangeSold)
        print('')
        print('Average Trade Size:', '${:0,.2f}'.format(statistics.mean(totalSharesTraded)))
        print('Median Trade Size:', '${:0,.2f}'.format(statistics.median(totalSharesTraded)))

        top10 = []
        for stock in stockData:
            top10.append([stock.symbol,stock.symbolBought+stock.symbolSold])
        def getSaleNum(item):
            return item[1]
        top10 = sorted(top10,key=getSaleNum)
        if len(top10) > 10:
            top10 = top10[0:9]
        top10.reverse()
        print('10 Most Active Symbols:',top10)

if __name__ == '__main__':
    main()