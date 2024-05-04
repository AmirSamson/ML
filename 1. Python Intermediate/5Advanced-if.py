# We are running a themePark. we need the height and age of people. so we the Age and the Height:

# age = -1
# height = 140
# ticket = "Super"

# # For adding more conditions to the code and needing all the conditions in the code to validate the ride: 
# # we can start using the `and` in the `if` statements: 

# if age >= 8 and height >= 135: 
#     print("You are in!")

# # we can add more and more conditions by just adding `and` to the `if statement`.

# if age >= 9 and height >= 150 and ticket == "Super admin":
#     print("Yippies!")

# # For having one of the conditions in the `if statement` working, we can use `or`:

# if age >= 10 or height >= 170: 
#     print("we have got you covered!")

# # The ELIF concept (else if): the elif statement helps us to have an else inside an if.
# # like if you are below 120 cm, you cannot ride any rides. elif you are below 135cm you can oly ride the level-1 rides:
    
# if height < 120:
#     print ("You are too small for riding.")
# elif height <135:
#     print("you can only ride the Level-1 rides!")
# elif height <200:  # this means the cap for height is 200 cm and not above.
#     print("you can enjoy all the rides!!!")
# else: # this means that if you are anything other than 200 cm, you cannot use the rides.
#     print("You are too tall to ride!")



# -------------------------------------------------------------------------------------
##### EXercise: 

your_age = int(input("input your age: "))

if your_age % 2 == 0 and your_age > 100 or your_age == 0:
    print(your_age)
elif your_age < 100:
    print("your age is below 100")
elif your_age < 0:
    print("how come??")