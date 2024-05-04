import random

class Dogo: 
    info = "Doggo name is Fan"

    def __init__(self, name):             # When ever a new object is created from a class, this function is called. 
        print("hi")
        self.lucky_number = random.randint(1,10)
        self.name = name                           ### Hint: the `name` is defined in `def __init__(self, name)`


                        # in order to add a new instance, we can add it with the `def` and add it. 
                            # how to add other variables inside of it?? by adding them in the `Print` with the = f"[text]"

    def bark(self):
        print(f"waagh waagh. hi my name is {self.name} and I have {self.lucky_number} years old.")

dog1 = Dogo("Sammy")        # this means that we have defined dogo's name
dog2 = Dogo("Rick")

print(dog1.name)        # this means that we print the dogo name inside Dogo([name]), using the   Self.name    instnace
print(dog2.name)

dog1.bark()
dog2.bark()
print(Dogo.info)


# ----------------\
### Exercise: 

class New: 
    AAA = "shipped title"
    
    def Game(self):
        print(f"My Game rocks! And it's a {New.AAA}.")

G1 = New()
G1.Game()


# -------------------------


class Shoe:
    Length = 280

    def area(self):
        return self.width * self.Length
    
Addidas = Shoe()
Addidas.width = 40
print(f"{Addidas.area()} mm")


