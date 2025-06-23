class Computer:
    def __init__(self):
        self.__maxprice = 1050

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()


c.__maxprice = 1000
c.sell()

c.setMaxPrice(5000)
c.sell()

