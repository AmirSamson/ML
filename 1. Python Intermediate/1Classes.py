# class Dog:
#     info = "A furry animal." ---- in a class there can be multiple variables.
    
# Dog.info
#     def __init__(self):  # Whenever a new object is created from a class, this function is called. 
#         print("Iam Alive!")
        

# Dog()
# Dog()
# Dog()


# -------------

# import random

# class Dogo: 
#     info = "Doggo name is Fan"

#     def __init__(self):  # When ever a new object is created from a class, this function is called. 
#         print("hi")
#         print(random.randint(1,10))

# Dogo() # this is a new object

# -------------------------- 


### this is for creating a `self` instance Variable, which is in def __init__(self)

# import random

# class Dogo: 
#     info = "Doggo name is Fan"

#     def __init__(self):  # When ever a new object is created from a class, this function is called. 
#         print("hi")
#         self.lucky_numbr = random.randint(1,10)

# dog1 = Dogo() # "Dogo" is a new object
# dog1 = Dogo() # this only prints out the "hi" because Dogo is related to the def __init__ function and print is called every time we call Dogo()
# dog2 = Dogo()

# print(dog1.lucky_numbr)  # this means that we print the `self.lucky_number` (which is random) for for dog1 
# print(dog2.lucky_numbr)

# dog1.name = "Henn"  # we can have the instance variables for other things without needing to redefine them.
# print(dog1.name)

#---------------------

### we can have another   Self   instance which is related to "name" and here is how it works:

import random

class Dogo: 
    info = "Doggo name is Fan"

    def __init__(self, name):             # When ever a new object is created from a class, this function is called. 
        print("hi")
        self.lucky_numbr = random.randint(1,10)
        self.name = name                           ### Hint: the `name` is defined in `def __init__(self, name)`

dog1 = Dogo("Sammy")        # the name in "" is refering to the `name` variable in that def function. so that whenver it is called it will call the name of the dogo.
dog2 = Dogo("Rick")

print(dog1.name)        # this means that we print the dogo name inside Dogo("[name]"), using the   `Self.name`   instnace
print(dog2.name)


#--------------------- 

### Exercise::::: 

# class Exercise:
#     info = "this is an exercise"

#     def __init__(Self, Exe):
#         Self.name = Exe

# exe1 = Exercise("exercise 1 was great")
# exe2 = Exercise("Exercise 2 was difficult")

# print(exe1.name)
# print(exe2.name)


# # --------------------
# ### Exercise: make an instance of your previous class and add and instance variable/attribute to it. 

# class Amir:
#     weight = 87
#     Height =185

#     def __init__(self):
#         print(f"Amir has {Amir.weight} kilos and {Amir.Height}cm high.")

# Ghad = Amir()
# Ghad.Height = 184

# print(Ghad.Height)
# print(Amir.weight)

