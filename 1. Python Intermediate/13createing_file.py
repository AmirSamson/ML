# how to open a file? with a function called: `open`

### first Parameter is the name of the file.  second Parameter is the method. X means = Creates only if the file doesn't exists:
# file = open("amir.text", "x") 
# file.write("X marks the spot!")

# file.close() # we should close the opened file!!


# ----------------------------- 
### first Parameter is the name of the file.  second Parameter is the method.     W means = Overwrite
# file = open("amir.text", "w") 
# file.write("For the W!")

# file.close()

# ----------------------------- 
### first Parameter is the name of the file.  second Parameter is the method.     a means = append it.
# file = open("amir.text", "a") 
# file.write(" --- AAAAAAA ------- ")

# file.close()


import sys 

filename = sys.argv[1]
file = open(filename, "w")
file.write("this was the challeng!")
file.close()


# import sys 

# for argument in sys.argv[1]: 
#     file = open(f"{argument}.text", "x")
#     file.write("this is the challenge!")
#     file.close()