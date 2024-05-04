# # how to read a file?

# file = open("amir.txt" , "x")
# file.write("amir is awesome, and so do you")
# file.close()


# file = open("amir.txt", "r") # r stands for "read"

# file_text = file.read()
# print(file_text)

# lines = file.readlines()
# print(lines)

# file.close()


# ## another way for reading a file:::: using a For loop:

# file = open("amir.txt", "r")       # r stands for "read"

# for line in file:
#     print(line)

# file.close()


#### ------------------------------------------------------------------------------------------------------------------------

###### Challenge: 
    # read a file that has numbers, mlutipy all the numbers together and print it:

# two ways to do this.
    # 1st: use a `for loop` : 

files = open("14challenge.txt", "r")

total = 1
for linesss in files:
    try:
        number = int(linesss)
        total *= number
    except Exception as e: 
        pass

print(total)
files.close()



# two ways to do this.
    # 2nd: use Map and Reduce: 

from functools import reduce

with open("14challenge.txt", "r") as file:
    file_text = file.readlines()

strings = file_text.split('\n')
# file = open("14challenge.txt", "r")
# file_text = file.readlines()
# list = file_text.int()

strings_list = list(map(int(file_text.split('\n')), file_text))

# new_list = list(filter(lambda x: isinstance(x, int), strings))
# print(new_list)
print(strings_list)

# try:
#     read = reduce(lambda total, multipy: total * multipy, strings_list, 1)
# except Exception as e:
#     pass

# print(read)
file.close()


