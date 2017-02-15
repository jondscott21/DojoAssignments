class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print self.name
        print self.health
        return self
animal = Animal('tiger')
animal.walk().walk().walk().run().run().displayHealth()
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
beagle = Dog("Fido")
beagle.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
        super(Dragon, self).displayHealth()
        print('This is a dragon!')
    def fly(self):
        self.health -= 10
        return self
drogon = Dragon('drogon')
drogon.walk().walk().walk().run().run().fly().fly().displayHealth()
