class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax
honda = Car(5000, "120mph", "Full", 150000)
ferrari = Car(350000, "185mph", "Empty", 3000)
volt = Car(35000, "90mph", "I don't need no gas", 80000)
tesla = Car(140000, "155mph", "I don't need no gas", 2000)
hummer = Car(80000, "80mph", "Half full", 15000)
bmwI8 = Car(140000, "155mph", "3/4 full", 140)
honda.display_all()
ferrari.display_all()
volt.display_all()
tesla.display_all()
hummer.display_all()
bmwI8.display_all()
# pair programmed by arnold son, jon scott, jackie thind

