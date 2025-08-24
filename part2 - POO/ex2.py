class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} borned!")

    def comer(self):
        print(f"{self.name} is eating...")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is moewing: meow, meow!")


catOne = Cat(name = input("Cat name: "))
catOne.meow()
catOne.comer()