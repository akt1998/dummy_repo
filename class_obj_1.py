class Bike:
    #attributes
    name = "Hayabusa"
    body = "GEN III"
    engine = 1400
    price = 2000000

    #custom method
    def demo(self):
        print(self.name)
        print(self.body)
        print(self.engine)
        
    def amount(self, discount):
        print(self.price - (self.price * discount / 100))

obj = Bike()
obj.demo()

discount = 21.25
obj.amount(discount)

obj.price = 1750000
discount = 10
obj.amount(discount)
    
