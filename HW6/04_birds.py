class Bird:
    name=str
    def __init__(self,name):
        self.name=name
    def fly(self):
        print(f"{self.name} can fly!")
    def walk(self):
        print(f"{self.name} can walk!")

class FlyingBird(Bird):
    def __init__(self,name,food="grains"):
        Bird.__init__(self,name)
        self.ration=food
    def eat(self):
        print(f"{self.name} eats {self.ration}!")

class NonFlyingBird:
    def __init__(self,name,food="fish"):
        FlyingBird.__init__(self, name, food)
    def walk(self):
        Bird.walk(self)
    def eat(self):
        FlyingBird.eat(self)
    def swim(self):
        print(f"{self.name} can swim!")

class SuperBird:
    def __init__(self,name,food="everything"):
        FlyingBird.__init__(self,name,food)
    def fly(self):
        Bird.fly(self)
    def walk(self):
        Bird.walk(self)
    def swim(self):
        NonFlyingBird.swim(self)
    def eat(self):
        FlyingBird.eat(self)

def opt(str):
    Bird(str)
    FlyingBird(str)
    NonFlyingBird(str)
    SuperBird(str)

b = Bird("Any")
b.walk()

p = NonFlyingBird("Penguin", "fish")
p.swim()
p.eat()
p.walk()
c = FlyingBird("Canary")
opt(c)
c.eat()

s = SuperBird("Gull")
str(s)
s.eat()