class person(object):
    def __init__(self, personalMoney=None, portfolio=None):
        if personalMoney is None:
            personalMoney = 0
        if type(personalMoney) is not money:  # attempts to convert if proper format is not used
            personalMoney = money(personalMoney)
        self.personalMoney = personalMoney

        if portfolio is None:
            portfolio = {}
        if type(portfolio) is not dict:  # checks that all portfolio is a dict with stocks that have an integer amount
            raise TypeError("portfolio must be input as a dictionary")
        for current in portfolio:  # checks that portfolio contains stocks and that person owns integer number of stocks
            if type(current) is not stock:
                raise TypeError("Any stocks in your portfolio dictionary must be a type of stock")
            if type(portfolio[current].currentValue) is not money:
                portfolio[current].currentValue = money(portfolio[current].currentValue)
            if type(portfolio[current].purchasePrice):
                portfolio[current].purchasePrice = money(portfolio[current].purchasePrice)
            if type(portfolio[current].number) is not int:
                raise TypeError("Any stocks in your portfolio dictionary must have an integer amount")
        self.portfolio = portfolio

    def buy(self, stockToBuy, number=1):
        """
        Purchases a stock, saves the currentValue and number of stocks purchased.
        Default is 1
        """
        if type(stockToBuy) is not stock:  # checks inputs
            raise TypeError('Stock to buy must be a stock')
        if type(number) is not int:
            raise TypeError('You must buy an integer number of stocks')
        if self.personalMoney > stockToBuy.currentPrice * number:  # checks that person has enough money
            self.personalMoney -= stockToBuy.currentPrice * number
            if stockToBuy in self.portfolio:  # if the stock is already owned, just average the purchase price/share,
                # update current price and number
                averagePurchasePrice = ((self.portfolio[stockToBuy].purchasePrice * self.portfolio[
                    stockToBuy].number) + (stockToBuy.currentPrice * number)) / (
                                               self.portfolio[stockToBuy].number + number)
                self.portfolio[stockToBuy].purchasePriceSetter(averagePurchasePrice)
                self.portfolio[stockToBuy].currentValueSetter(stockToBuy.currentPrice)
                self.portfolio[stockToBuy].numberSetter(self.portfolio[stockToBuy].number + number)
            else:  # otherwise just create a stockInfoHolder for it
                self.portfolio[stockToBuy] = stockInfoHolder(stockToBuy.currentPrice, stockToBuy.currentPrice, number)
        else:
            raise ValueError("You don't have enough money for this. Please consider selling stocks or getting a loan")

    def sell(self, stockToSell, number=None):
        """
        sells a stock, increases personalMoney based on number of stocks sold.
        Default is all
        """
        if type(stockToSell) is not stock:  # checks inputs
            raise TypeError('Stock to sell must be a stock')
        if stockToSell not in self.portfolio:
            raise ValueError(str(stockToSell) + ' not owned.')
        if number is None:
            number = self.portfolio[stockToSell].number
        if type(number) is not int:
            raise TypeError('You must buy an integer number of stocks')
        if number > self.portfolio[stockToSell].number:
            raise ValueError("You don't own that many shares to sell")
        # if stockToSell is a stock that the person owns, and number is an integer number of stocks the person owns
        self.updateStockPrice(stockToSell)  # updates stocks price
        income = self.potentialIncome(stockToSell, number)
        self.personalMoney += income
        self.portfolio[stockToSell].number -= number  # removes shares from portfolio
        if self.portfolio[stockToSell].number == 0:  # if there are no shares left, removes the stock from portfolio
            del self.portfolio[stockToSell]
        print("Sold " + str(number) + " shares of " + str(stockToSell) + " for " + str(
            income) + ". \nCurrent Money: " + str(self.personalMoney))

    def sellTo(self, otherPerson, stockToSell, number=None):  # test this
        """
        Sells a stock to another person instead just selling.
        Default is 1 share
        """
        if type(otherPerson) is not person:
            raise TypeError("Please enter a person to sell to")
        if type(stockToSell) is not stock:
            raise TypeError("Please enter a stock to buy")
        if number is None:
            number = 1
        if type(number) is not int:
            raise TypeError("Please enter an integer number of stocks to sell")
        if otherPerson.personalMoney >= self.potentialIncome(stockToSell, number):  # checks that other person can
            # afford to buy the stocks
            self.sell(stockToSell, number)  # you sell
            otherPerson.buy(stockToSell, number)  # they buy

    def buyFrom(self, otherPerson, stockToBuy, number=None):  # test this
        """
        Buys stocks from another person instead of just buying.
        Default is 1 share
        """
        if type(otherPerson) is not person:
            raise TypeError("Please enter a person to sell to")
        if type(stockToBuy) is not stock:
            raise TypeError("Please enter a stock to buy")
        if number is None:
            number = 1
        if type(number) is not int:
            raise TypeError("Please enter an integer number of stocks to sell")
        if self.personalMoney >= otherPerson.potentialIncome(stockToBuy, number):  # ensures you can afford the stocks
            otherPerson.sell(stockToBuy, number)  # they sell
            self.buy(stockToBuy, number)  # you buy

    def potentialProfit(self, stockToSell=None, number=None):  # returns income - startingPrice paid if a stock is sold.
        """
        If there is an input for the stock, only return potential profit for that stock and the number of shares
        designated to be sold. If there is no input for the number, return the profit of all shares of the stock.
        If there is no input for either, return the potential profit for the entire portfolio
        """
        if stockToSell is None and number is None:
            profit = money(0)
            for current in self.portfolio:  # goes through each stock in the portfolio
                self.updateStockPrice(current)  # updates stock price
                profit += (self.portfolio[current].currentValue - self.portfolio[current].purchasePrice) * \
                          self.portfolio[current].number
            return profit

        if type(stockToSell) is not stock:  # checks inputs
            raise TypeError('Stock to sell must be a stock')
        if stockToSell not in self.portfolio:
            raise ValueError(str(stockToSell) + ' not owned.')
        if number is None:  # sets default to maximum number of shares that can be sold, none wouldn't be valid,
            # so it sets to default
            number = self.portfolio[stockToSell].number
        if type(number) is not int:
            raise TypeError('You must buy an integer number of stocks')
        if number > self.portfolio[stockToSell].number:
            raise ValueError("You don't own that many shares to sell")

        self.updateStockPrice(stockToSell)  # updates stock price
        return (self.portfolio[stockToSell].currentValue - self.portfolio[stockToSell].purchasePrice) * number

    def potentialIncome(self, stockToSell=None, number=None):
        """
        Returns income is a stock is sold. Default is all
        If there is an input for the stock, only return potential profit for that stock and the number of shares
        designated to be sold. If there is no input for the number, return the profit of all shares of the stock.
        If there is no input for either, return the potential profit for the entire portfolio
        """
        if stockToSell is None and number is None:  # if no inputs, return potential profit for the entire portfolio
            profit = money(0)
            for current in self.portfolio:  # goes through each stock in the portfolio
                self.updateStockPrice(current)
                profit += self.portfolio[current].currentValue * self.portfolio[current].number
            return profit

        if type(stockToSell) is not stock:  # checks inputs
            raise TypeError('Stock to sell must be a stock')
        if stockToSell not in self.portfolio:
            raise ValueError(str(stockToSell) + ' not owned.')
        if number is None:  # sets default to maximum number of shares that can be sold, none wouldn't be valid,
            # so it sets to default
            number = self.portfolio[stockToSell].number
        if type(number) is not int:
            raise TypeError('You must buy an integer number of stocks')
        if number > self.portfolio[stockToSell].number:
            raise ValueError("You don't own that many shares to sell")

        self.updateStockPrice(stockToSell)  # updates stock price
        return self.portfolio[stockToSell].currentValue * number

    def netWorth(self):
        """
        Returns value of a person's portfolio and money.
        """
        return self.personalMoney + self.potentialIncome()  # stock prices are updates in potentialIncome

    def updateStockPrice(self, currentStock):
        """
        Updates currentValue of stock. Should probably be called most of the time anything in this class is called
        except buying. Stock prices should always be accurate when selling, or checking income, but does not need to run
        when buying because the stock isn't there to update
        """
        if type(currentStock) is not stock:
            raise TypeError("Please input a stock")
        if currentStock not in self.portfolio:
            raise ValueError(str(currentStock) + " is not in this individual's portfolio")
        self.portfolio[currentStock].currentValueSetter(currentStock.currentPrice)

    def __str__(self):  # prints both the person's money and their stock portfolio
        return 'Money: ' + str(self.personalMoney) + '\nportfolio: ' + str(self.portfolio)


class money(object):
    def __init__(self, inputAmount):
        if type(inputAmount) is float or type(inputAmount) is int:  # ensures numerical input
            self.amount = inputAmount
        elif type(inputAmount) is money:
            self.amount = inputAmount.amount
        else:  # rejects any non numerical inputs
            raise TypeError('Prices must be in integer or float format.')

        self.basePrice = self.amount  # sets base price for discounts to be set

    def discount(self, percent):  # allows stock to be discounted, probably won't really use
        if type(percent) is not int and type(percent) is not float:
            raise TypeError('Discount percentage must be an integer or float')
        priceReduction = (abs(percent) * self.amount) / 100  # absolute value prevents accidentally increasing price
        self.amount = self.amount - priceReduction  # reduces price by discount amount

    def discountReset(self):  # resets amount
        self.amount = self.basePrice

    def newPrice(self, newBasePrice):  # sets new base price and amount for money, stocks have their own price update
        # method
        if type(newBasePrice) is int or type(newBasePrice) is float:
            self.basePrice = newBasePrice
            self.discountReset()  # resets amount
        else:  # rejects any non numerical inputs
            raise TypeError('Prices must be in integer or float format.')

    def __add__(self, other):
        if type(other) is money:
            return money(self.amount + other.amount)
        elif type(other) is float or type(other) is int:
            return money(self.amount + other)

    def __sub__(self, other):
        if type(other) is money:
            if other.amount > self.amount:  # if loans are implemented, use this
                raise ValueError("You don't have enough money for this")
            return money(self.amount - other.amount)
        elif type(other) is float or type(other) is int:
            if other > self.amount:
                raise ValueError("You don't have enough money for this")
            return money(self.amount - other)

    def __mul__(self, other):
        if type(other) is money:
            return money(self.amount * other.amount)
        elif type(other) is float or type(other) is int:
            return money(self.amount * other)

    def __truediv__(self, other):
        if type(other) is money:
            return money(self.amount / other.amount)
        elif type(other) is float or type(other) is int:
            return money(self.amount / other)

    def __gt__(self, other):
        if type(other) is money:
            if self.amount > other.amount:
                return True
        elif type(other) is int or type(other) is float:
            if self.amount > other:
                return True
        else:
            raise TypeError('Comparisons can only be made between money and numbers')

        return False  # condition if anything fails

    def __ge__(self, other):
        if type(other) is money:
            if self.amount >= other.amount:
                return True
        elif type(other) is int or type(other) is float:
            if self.amount >= other:
                return True
        else:
            raise TypeError('Comparisons can only be made between money and numbers')

        return False  # condition if anything fails

    def __lt__(self, other):
        if type(other) is money:
            if self.amount < other.amount:
                return True
        elif type(other) is int or type(other) is float:
            if self.amount < other:
                return True
        else:
            raise TypeError('Comparisons can only be made between money and numbers')

        return False  # condition if anything fails

    def __le__(self, other):
        if type(other) is money:
            if self.amount <= other.amount:
                return True
        elif type(other) is int or type(other) is float:
            if self.amount <= other:
                return True
        else:
            raise TypeError('Comparisons can only be made between money and numbers')

        return False  # condition if anything fails

    def __eq__(self, other):
        if type(other) is money:
            if self.amount == other.amount:
                return True
        elif type(other) is int or type(other) is float:
            if self.amount == other:
                return True
        else:
            raise TypeError('Comparisons can only be made between money and numbers')

        return False

    def __ne__(self, other):
        if type(other) is money:
            if self.amount != other.amount:
                return True
        elif type(other) is int or type(other) is float:
            if self.amount != other:
                return True
        else:
            raise TypeError('Comparisons can only be made between money and numbers')

        return False

    def __str__(self):
        return '$' + str(round(self.amount, 2))


class stock(object):
    def __init__(self, name, currentPrice):
        if type(name) is not str:
            raise TypeError("Stock name must be a string")
        self.name = name
        if type(currentPrice) is not money:
            currentPrice = money(currentPrice)
        self.currentPrice = currentPrice

    def nameSetter(self, newName):
        assert type(newName) is str
        self.name = newName

    def updatePrice(self, newPrice=None):
        if newPrice is None:  # if method is called with no input, asks user to provide an input
            newPrice = float(input('Input new price for ' + str(self.name) + ': '))
        if type(newPrice) is not money:  # converts to float first to get rid of string from input
            newPrice = money(newPrice)
        self.currentPrice = newPrice

    def __str__(self):
        return str(self.name) + ': Now worth: ' + str(self.currentPrice)


class stockInfoHolder(object):  # saves the original purchase price, allows the value to change, and holds the number
    # of stocks owned
    def __init__(self, purchasePrice, currentValue, number=1):
        if type(purchasePrice) is not money:
            purchasePrice = money(purchasePrice)
        if purchasePrice < 0:
            raise ValueError("You cannot purchase a stock for a negative amount of money")
        self.purchasePrice = purchasePrice

        if type(currentValue) is not money:
            currentValue = money(currentValue)
        if currentValue < 0:
            raise ValueError("A stock cannot be worth a negative amount of money")
        self.currentValue = currentValue

        if type(number) is not int:
            raise TypeError("You must buy an integer number of stocks")
        if number < 0:
            raise ValueError("You cannot own a negative number of stocks")
        self.number = number

    def purchasePriceSetter(self, purchasePrice):  # changes purchasePrice in stockInfoHolder
        if type(purchasePrice) is not money:
            purchasePrice = money(purchasePrice)
        if purchasePrice < 0:
            raise ValueError("You cannot purchase a stock for a negative amount of money")
        self.purchasePrice = purchasePrice

    def currentValueSetter(self, currentValue):  # changes currentValue in stockInfoHolder
        if type(currentValue) is not money:
            currentValue = money(currentValue)
        if currentValue < 0:
            raise ValueError("A stock cannot be worth a negative amount of money")
        self.currentValue = currentValue

    def numberSetter(self, number):  # changes number of stocks in stockInfoHolder
        if type(number) is not int:
            raise TypeError("You must buy an integer number of stocks")
        if number < 0:
            raise ValueError("You cannot own a negative number of stocks")
        self.number = number

    def __str__(self):
        return 'Purchase: ' + str(self.purchasePrice) + " Value: " + str(self.currentValue) + " Shares: " + str(
            self.number)


class loan(object):  # implement to avoid negative money
    pass


preset = True
if preset is True:
    # stock testing - should work
    Tesla = stock('TSLA', 10.257)  # more than 3 trailing digits
    Amazon = stock('AMZN', 120)  # integer
    Google = stock('GOOG', 25.3)  # only 1 trailing digit

    # stock testing - shouldn't work
    # stringStock = stock('TACO','5') # string for value - Throws proper error
    # wrongNameStock = stock(5, 123)  # int for name - Throws proper error

    # stockInfoHolder testing - should work
    brandiStockInfo = {Tesla: stockInfoHolder(2.50, Tesla.currentPrice),
                       Amazon: stockInfoHolder(10, Amazon.currentPrice),
                       Google: stockInfoHolder(5, Google.currentPrice, 50)}

    # stockInfoHolder testing - shouldn't work
    # brookeStockInfo = {'Fake': stockInfoHolder(1.00, 5, 9)}  # info for a fake stock - throws error with Fake as stock
    # brooke = person(0, brookeStockInfo)  # throws error with Fake as string
    # poo = person(10, {Tesla: stockInfoHolder(5, 5, -4)})  # has a negative number of shares - throws error
    # tony = person(5000, {Tesla: stockInfoHolder(5, -1)})  # has a negative currentValue - throws error

    # person testing should work
    test = person()  # blank person
    brandi = person(2564.56, brandiStockInfo)  # float money and info from above
    nathan = person(5000)

    # buy testing
    # test.buy(Tesla) # test doesn't have enough money - throws proper error
    # notReal.buy(Google) # not real person - throws proper error
    nathan.buy(Tesla)
    # nathan.buy(Tesla,5.5) #non integer number of stocks to buy - throws proper error
    brandi.buy(Tesla, 23)

    # potentialProfit testing
    # print("Tesla Potential Profit for Brandi: " + str(brandi.potentialProfit(Tesla))) # has potential profit since
    # currentValue is higher than purchasePrice
    # Tesla.updatePrice(50)
    # print("Updated Tesla Value, new Potential Profit for Brandi: " + str(brandi.potentialProfit(Tesla))) # increases
    # potential profit since currentValue has gone up
    # print("Potential Profit for Nathan: " + str(nathan.potentialProfit()))  # 0 since the currentValue is the
    # same as purchasePrice
    # nathan.buy(Tesla, 4)
    # print("Potential Profit for Nathan after buying Tesla: " + str(nathan.potentialProfit()))  # stays at 0 since the
    # currentValue is the same as purchasePrice
    # Tesla.updatePrice(100)
    # print("Potential Profit for Nathan after Tesla price update: " + str(nathan.potentialProfit()))  # potential
    # profit increases now since the currentValue of Tesla has now gone up

    # income testing
    # print("Potential Income for Nathan: " + str(nathan.potentialIncome()))
    # nathan.buy(Google, 10)
    # print("Potential Income for Nathan after buying Google: " + str(nathan.potentialIncome(Google)))
    # nathan.buy(Amazon, 3)
    # print("Potential Income for Nathan after buying Amazon: " + str(nathan.potentialIncome()))
    # print("Brandi Potential Income: " + str(brandi.potentialIncome()))
    # Amazon.updatePrice(100)
    # print("Brandi Potential Income after lowering Amazon Price $20: " + str(brandi.potentialIncome()))

    # net worth testing
    # print("Brandi's net worth: " + str(brandi.netWorth()))
    # Tesla.updatePrice(50)
    # Google.updatePrice(500)
    # print("Brandi's net worth after stock price increase: " + str(brandi.netWorth()))
    # brandi.sell(Tesla)
    # brandi.sell(Google)
    # print("Brandi's net worth after selling stock: " + str(brandi.netWorth()))

    # sellTo testing
    nathan.sellTo(brandi,Tesla) # default arguments
    brandi.buy()
    # buyFrom testing
