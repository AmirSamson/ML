import pickle

age = 320320

file = open("text.txt", "wb")   # `b` stands for binary data. for pickling we should use "wb".... but it saves binary data.
pickle.dump(age, file)
file.close()


# For reading it our correctly we need to use the read in Open function:    ((but not "r", this time its "rb" for reading binary))

file = open("text.txt", "rb")
new_age = pickle.load(file)
file.close()

print(new_age)