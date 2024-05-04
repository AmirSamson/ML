# THis is Inheritance. this means that we create a Parent class and create childs of it (other classes) 
# which can Inherit the attributes of the Parent class. 

import random

class Animal:
    info = "A living organism that feeds on organic matter."

    def __init__(self, name):
        print("An animal is dispached")
        self.name = name                           ### Hint: the `name` is defined in `def __init__(self, name)`

class Dogo(Animal): 
    info = "Doggo name is Fan"

    def __init__(self,name):             # When ever a new object is created from a class, this function is called. 
        super().__init__(name)
        print("A Dog is on the battlefield.")
        self.lucky_number = random.randint(1,10)
        


                        # in order to add a new instance, we can add it with the `def` and add it. 
                            # how to add other variables inside of it?? by adding them in the `Print` with the = f"[text]"

    def bark(self):
        print(f"waagh waagh. hi my name is {self.name} and I have {self.lucky_number} years old.")

dog1 = Dogo("Sammy")        # this means that we have defined dogo's name