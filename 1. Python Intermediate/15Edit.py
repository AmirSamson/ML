
# Hello         I added content in the middle lines so first read the top, then bottom, then middle (for #Edit part)
# for editing a file we can use the "w+" or "r+".  but each has a unique usage:


# file = open("amir.txt", "x")
# file.write("Hey hey hey!")
# file.close()

# Read
# file = open("amir.txt", "r")
# lines = file.readlines()
# file.close()


# Edit

# lines = ["Hello", "My name is Amir"]   # this will put all of the text as in one line (it suppose to be a list and two lines)

# in order to do this we should write the code like this:
# lines = ["Hello\n", "my name is amir"]



# 2 --------- How to add another line to the text in the file, without overwriting it?? 
# we do this: 
# (First we should comment the previous ` lines = ["Hello\n", "my name is amir"]` 
# because the "w" will overwrite everything we add so we need to comment that out, to only  have the insertion. as the following)


# lines.insert(3, "\nI love your coat!\n")


# 3 --------- How to change a line (change a text) to the text in the file? 
# we do this: 
# (First we should comment the previous `lines.insert(3, "\nI love your coat!\n")` :
# if we want to add an edit in the line 2, so we need to add [1] to the lines = .... 

# lines[1] = "My name is Amir, and I will be assissting you in this!\n"


# 4 --------- How to add an extra line at the end of the file? 
# we do this: 
# (First we should comment the previous `lines[1] = "My name is Amir, and I will be assissting you in this!\n"` :
# if we want to add a line and then add an extra line, so that everytime our file creates another line. we should first use the [-1] trick: 

# lines[-1] = lines[-1] + "\n"        # this will add a new line at the end of the file

# # now we can append an extra text: 
# lines.append("Goodbye, mate!")


# Write
# file = open("amir.txt", "w")
# file.writelines(lines)      # this will take all of the lines we have in the list and will write it to the file. 
# file.close()





############ Challenge: 
            # create a file: "numbers.txt", add numbers to it. and multipy each number by 2: 


file = open("numbers.txt", "r")
lines = file.readlines()
file.close()

for x in range(len(lines)):
    try:
        numbers = float(lines[x]) * 2
        lines[x] = f"{numbers}\n"
    except Exception as e: 
        pass

# Write
file = open("numbers.txt", "w")
file.writelines(lines)      # this will take all of the lines we have in the list and will write it to the file. 
file.close()
