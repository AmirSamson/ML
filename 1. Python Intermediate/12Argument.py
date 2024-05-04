import sys
# Argument is the name of the file that we have. exp: this file name is 12Argument.py. 
# so whenever we run the command of 'python .\12Argument.py' , this will take the name of the file. 

# for argument in sys.argv:
#     print(argument)

### Challenge: 
    #take the numbers in argument and multipy them together:

# totall = 1
# for argument in sys.argv:
#     try:
#         number = int(argument)
#         totall = totall * number
#     except:
#         pass
# print(totall)

totall = 1
del(sys.argv[0])
for argument in sys.argv:
    try:
        number = float(argument)
        totall = totall * number
    except Exception as e:
        print(e)
        print("only numbers can be provided!")
        sys.exit(1)  ### this means that if there is an error, the program will exit --> exit(1) means that there is an error. 
print(totall)

