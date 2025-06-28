class computer:
    def __init__(self):
        self.maxprice = 1500

    def sell(self):
        print("Selling price : {}".format(self.maxprice))

    def setmaxprice(self , price):
        self.maxprice = price

c = computer()
c. sell()

c.__maxprice = 2000
c.sell()
c.setmaxprice(2500)
c.sell()