class person(object):
    def __init__(self, personalMoney=0, stocks=None):
        if type(personalMoney) is not money:  # attempts to convert if proper format is not used
            personalMoney = money(personalMoney)
        self.personalMoney = personalMoney

        if stocks is None:
            stocks = {}
        if type(stocks) is not dict:  # checks that all stocks is a dict with items that have an integer amount
            raise TypeError("Stocks must be input as a dictionary")
        for current in stocks:
            if type(current) is not item and type(current) is not combinedItem:
                raise TypeError("Any items in your stocks dictionary must be a type of item")
            if type(stocks[current]) is not int:
                raise TypeError("Any items in your stocks dictionary must have an integer amount")
        self.stocks = stocks

    # FIXME methods below need to be added
    def use(self, itemUsed, numberUsed=1):  # uses 1 of an item by default, can use more
        if type(itemUsed) is item or type(itemUsed) is combinedItem:
            if itemUsed not in self.stocks:
                raise ValueError('This person does not have any ' + str(itemUsed))
            if itemUsed in self.stocks and self.stocks[itemUsed] >= numberUsed:
                self.stocks[itemUsed] -= numberUsed
            else:
                raise ValueError('There are not enough ' + self.stocks + 's for this.')
        else:
            raise TypeError('Please input an item to search for')

    def quantitySetter(self, currentItem, newQuantity):
        assert type(currentItem)
        assert type(newQuantity) is int
        self.stocks[] = newQuantity

    def buy(self, itemToBuy, number=1):  # increases the quantity available of an item
        assert type(itemToBuy) is item or combinedItem
        assert type(number) is int
        if self.amount < itemToBuy.salePrice * number:
            self.amount += itemToBuy.salePrice * number
        #    purchaser.amount -= (self.cost * number).amount
        else:
            print('Operation Failed')

    def sell(self, seller, number=1):
        for current in self.inputs:  # checks that there is enough of everything before using it
            if current.quantityInStock < number:
                raise ValueError('There is not enough ' + str(current.name) + ' for this')

        for currentItem in self.inputs:  # actually uses the items required
            currentItem.use(number)

        if type(seller) is not money:
            raise ValueError("The seller must be a money account")
        else:
            seller.amount += (self.itemSalePrice * number).amount

    def potentialProfit(self):  # FIXME returns maximum profit if all available units are sold of all items/ Net Worth?
        return round((self.itemSalePrice - self.totalCost) * self.maxAvailable(), 2)

    def __str__(self):
        return 'Money: ' + str(self.personalMoney) + '\nstocks: ' + str(self.stocks)


class money(object):
    def __init__(self, inputAmount):
        if type(inputAmount) is float or type(inputAmount) is int:  # rounds any floating point value to 2 decimal
            # points to represent cents
            self.amount = round(inputAmount, 2)
        elif type(inputAmount) is money:
            self.amount = inputAmount.amount
        else:  # rejects any non numerical inputs
            raise TypeError('Prices must be in integer or float format.')
        self.basePrice = round(inputAmount, 2)  # sets base price for discounts to be set

    def discount(self, percent):  # allows item to be discounted
        if type(percent) is not int and type(percent) is not float:
            raise TypeError('Discount percentage must be an integer or float')
        priceReduction = (abs(percent) * self.amount) / 100  # absolute value prevents accidentally increasing price
        self.amount = round(self.amount - priceReduction, 2)  # reduces price by discount amount

    def discountReset(self):  # gets rid of discount on item
        self.amount = self.basePrice

    def newPrice(self, newBasePrice):  # sets new base price for item
        if type(newBasePrice) is int or type(newBasePrice) is float:
            self.basePrice = round(newBasePrice, 2)
            self.discountReset()
        else:  # rejects any non numerical inputs
            raise TypeError('Prices must be in integer or float format.')

    def __add__(self, other):
        if type(other) is money:
            return money(self.amount + other.amount)
        elif type(other) is float or type(other) is int:
            return money(self.amount + other)

    def __sub__(self, other):
        if type(other) is money:
            if other.amount > self.amount:
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
        return '$' + str(self.amount)


class item(object):
    def __init__(self, name, sellPrice, buyPrice):
        assert type(name) is str
        self.name = name
        if type(sellPrice) is not money:
            sellPrice = money(sellPrice)
        self.sellPrice = sellPrice
        if type(buyPrice) is not money:
            buyPrice = money(buyPrice)
        self.cost = buyPrice

    def nameSetter(self, newName):
        assert type(newName) is str
        self.name = newName

    def costSetter(self, newCost):
        if type(newCost) is not money:
            newCost = money(newCost)
        self.cost = newCost

    def __str__(self):
        return str(self.name) + ': Sell For: ' + str(self.sellPrice) + '/' + str(self.name) + ' Cost/' + str(
            self.name) + ': ' + str(
            self.cost)


# Not using this class right now, shifting to stocks
class combinedItem(object):
    def __init__(self, name, inputList, salePrice):
        assert type(name) is str
        self.name = name
        assert type(inputList) is list
        self.totalCost = money(0)
        for currentItem in inputList:
            assert type(currentItem) is item
            self.totalCost += currentItem.cost
        self.inputs = inputList
        if type(salePrice) is not money:
            salePrice = money(salePrice)
        self.itemSalePrice = salePrice
        self.currentMax = self.maxAvailable()

    def maxAvailable(self):  # FIXME going to have to check through items in person's stocks dict
        self.currentMax = float('inf')
        for currentItem in self.inputs:  # finds lowest quantity
            if currentItem.quantityInStock < self.currentMax:
                self.currentMax = currentItem.quantityInStock
        return self.currentMax

    def potentialProfit(self):  # returns maximum profit if all available units are sold
        return round((self.itemSalePrice - self.totalCost) * self.maxAvailable(), 2)

    def priceSetter(self, newPrice):
        self.itemSalePrice = money(newPrice)

    def __str__(self):  # prints the item, the quantity, the price it's sold at, and the cost to produce it
        return str(self.name) + ': Max Available: ' + str(self.maxAvailable()) + ' Price: ' + str(
            self.itemSalePrice) + ' Cost: ' + str(self.totalCost)


preset = True
if preset is True:
    Tesla = item('TSLA', 10, 8)
    nathan = person(0, stocks={tomato: 5})

# convert sell method to be a part of money and take combinedItem
# convert buy method to take item or combinedItem
# fix rounding issue (goes to $106.28999999 instead of $106.29 after selling a salad
