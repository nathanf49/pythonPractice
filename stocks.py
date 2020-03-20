class person(object):
    def __init__(self, personalMoney=0, portfolio=None):
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

    def buy(self, stockToBuy,
            number=1):  # purchases a stock, saves the currentValue and number of stocks purchased. Default is 1
        if type(stockToBuy) is not stock:
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
                self.portfolio[stockToBuy].purchasePrice = averagePurchasePrice
                self.portfolio[stockToBuy].currentValue = stockToBuy.currentPrice
                self.portfolio[stockToBuy].number += number
            else:  # otherwise just create a stockInfoHolder for it
                self.portfolio[stockToBuy] = stockInfoHolder(stockToBuy.currentPrice, stockToBuy.currentPrice, number)
        else:
            raise ValueError(
                "You don't have enough money for this. Please consider selling stocks or taking out a loan")

    def __str__(self):
        return 'Money: ' + str(self.personalMoney) + '\nportfolio: ' + str(self.portfolio)


class money(object):
    def __init__(self, inputAmount):
        if type(inputAmount) is float or type(inputAmount) is int:  # rounds any floating point value to 2 decimal
            # points to represent cents
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
            # if other.amount > self.amount:                              #if loans are implemented, use this
            #    raise ValueError("You don't have enough money for this")
            return money(self.amount - other.amount)
        elif type(other) is float or type(other) is int:
            # if other > self.amount:
            #   raise ValueError("You don't have enough money for this")
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
        self.purchasePrice = purchasePrice
        if self.purchasePrice < 0:
            raise ValueError("You cannot purchase a stock for a negative amount of money")

        if type(purchasePrice) is not money:
            currentValue = money(currentValue)
        self.currentValue = currentValue
        if self.currentValue < 0:
            raise ValueError("A stock cannot be worth a negative amount of money")

        if type(number) is not int:
            raise TypeError("You must buy an integer number of stocks")
        self.number = number
        if self.number < 0:
            raise ValueError("You cannot own a negative number of stocks")

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
    brandiStockInfo = {Tesla: stockInfoHolder(2.50, Tesla.currentPrice)}

    # stockInfoHolder testing - shouldn't work
    # brookeStockInfo = {'Fake': stockInfoHolder(1.00, 5, 9)}  # info for a fake stock - throws error with Fake as stock
    # brooke = person(0, brookeStockInfo)  # throws error with Fake as string
    poo = person(10, {Tesla: stockInfoHolder(5, 5, -4)})  # has a negative number of shares
    tony = person(5000, {Tesla: stockInfoHolder(5, -1)})  # has a negative currentValue

    # person testing should work
    nathan = person()  # blank person
    brandi = person(2564.56, brandiStockInfo)  # float money and info from above

    # write more tests

    # buy testing
    nathan.buy(Tesla)

    Tesla.updatePrice(50)
    nathan.buy(Tesla, 4)


    # implement price changes updating to calculate profit for individuals and keep working down method list

    # FIXME methods below need to be added to person

    def use(self, stockUsed, numberUsed=1):  # uses 1 of an stock by default, can use more
        if type(stockUsed) is stock:
            if stockUsed not in self.portfolio:
                raise ValueError('This person does not have any ' + str(stockUsed))
            if stockUsed in self.portfolio and self.portfolio[stockUsed] >= numberUsed:
                self.portfolio[stockUsed] -= numberUsed
            else:
                raise ValueError('There are not enough ' + self.portfolio + 's for this.')
        else:
            raise TypeError('Please input an stock to search for')


    def quantitySetter(self, currentstock, newQuantity):
        assert type(currentstock) is stock
        assert type(newQuantity) is int
        self.portfolio[currentstock] = newQuantity


    def sell(self, seller, number=1):
        for current in self.inputs:  # checks that there is enough of everything before using it
            if current.quantityInStock < number:
                raise ValueError('There is not enough ' + str(current.name) + ' for this')

        for currentstock in self.inputs:  # actually uses the stocks required
            currentstock.use(number)

        if type(seller) is not money:
            raise ValueError("The seller must be a money account")
        else:
            seller.amount += (self.stockSalePrice * number).amount


    def potentialProfit(self):  # FIXME returns maximum profit if all available units are sold of all stocks/ Net Worth?
        return round((self.stockSalePrice - self.totalCost) * self.maxAvailable(), 2)
