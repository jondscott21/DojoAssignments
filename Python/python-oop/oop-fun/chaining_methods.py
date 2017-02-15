class Bike(object):
    def __init__(self, price, max_speed, total_miles=0):
        self.price = price
        self.max_speed = max_speed
        self.total_miles = total_miles
    def display_info(self):
        print "Price:", self.price, "Max speed:", self.max_speed, "Total miles:", str(self.total_miles)
        return self
    def ride(self):
        print "Riding"
        self.total_miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.total_miles -= 5
        return self
huffy = Bike("50", "8mph")
specialized = Bike("1000", "50mph", 50)
stolen_bike = Bike('Five finger discount', '10mph', 1000)
specialized.ride().ride().ride().reverse().reverse().reverse().display_info()
# pair programmed by arnold son, jon scott, jackie thind