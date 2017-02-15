class Bike(object):
    def __init__(self, price, max_speed, total_miles=0):
        self.price = price
        self.max_speed = max_speed
        self.total_miles = total_miles
    def display_info(self):
        print "Price:", self.price, "Max speed:", self.max_speed, "Total miles:", str(self.total_miles)
    def ride(self):
        print "Riding"
        self.total_miles += 10
    def reverse(self):
        print "Reversing"
        self.total_miles -= 5
huffy = Bike("50", "8mph")
specialized = Bike("1000", "50mph", 50)
stolen_bike = Bike('Five finger discount', '10mph', 1000)
huffy.display_info()
huffy.ride()
huffy.display_info()
huffy.reverse()
huffy.display_info()
specialized.display_info()
specialized.ride()
specialized.display_info()
specialized.reverse()
specialized.display_info()
stolen_bike.display_info()
stolen_bike.ride()
stolen_bike.display_info()
stolen_bike.reverse()
stolen_bike.display_info()
# pair programmed by arnold son, jon scott, jackie thind