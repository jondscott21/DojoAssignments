class MathDojo(object):
    def __init__(self):
        pass
    def add(self, a, b):
        print a + b
        return self
    def subtract(self, x=0, y=0):
        print x - y
        return self
    def result(self):
        pass
md = MathDojo()
md.add(4, 5).subtract(3, 7 )
