class computer:
    def __init__(self):
        self.maxprice = 900
    def sell(self):
        print("Selling price :{}".format(self.maxprice))
    def setMaxPrice(self,price):
        self.maxprice = price

c = computer()
c.sell()

c.maxprice=1000
c.sell()

c.setMaxPrice(1000)
c.sell()