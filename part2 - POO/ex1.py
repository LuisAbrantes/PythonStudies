class Dog():
    def __init__(self, dogName, dogColor):
        self.name = dogName
        self.color = dogColor
    
    def bark(self):
        print(f"{self.name} is barking: wof wof")
        
dogOne = Dog(dogName=input("What is the dog name? "), dogColor=input("What is the dog color? "))
dogTwo = Dog(dogName=input("What is the dog name? "), dogColor=input("What is the dog color? "))

print(f"The dog1 name is {dogOne.name} and its color is {dogOne.color}")
print(f"The dog2 name is {dogTwo.name} and its color is {dogTwo.color}")

dogOne.bark()
dogTwo.bark()