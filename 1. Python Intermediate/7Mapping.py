class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score 
        
    def list(self):
        print(student_results)

# lets create a list:
        
students = [student("Amir", 0.16), student("Ali", 0.14), student("Samson", 0.19), student("Milad", 0.20), student("Hesam", 0.15)] 

# The list above is indicating the students name and their score number.
# now lets create a `For loop` to know who passed the test: 

student_results = []

for student in students:
    # if student.score >= 0.15:
    #     student_results.append(f"{student.name} Passed!")
    # else:
    #     student_results.append(f"{student.name} Failed!")



#### How we shorten this `For loop` in one line? by the following method: 

    # We take the true statement `student_results.append(f"{student.name} Passed!")` put the `if statement` after it and then the `else` part:

    student_results.append(f"{student.name} Passed!") if student.score >= 0.15 else student_results.append(f"{student.name} Failed!")

student.list()

#### NOW --> For maping the data out of the `Student list` we can use `map`. it has a `lambda` function inside it. and only needs the list of students:
                        # Lambda function = a parameter [x or whatever name]: parameter[x or whatever name], list[students]
        # Like this: map(lambda , students)

# to make it readable, we should craete it as a list =====> list(map(lambda....))
## and to print it, we use it as an Object: 

                # map_results = list(map(lambda student: student.name, students))
                # print(map_results)

### but we want to short the code lines! so here is the trick: 
        # take out the code on line 30 and paste it in the `lambda function`. without the append() part: 

map_results = list(map(lambda student: f"{student.name} Passed!" if student.score >= 0.15 else f"{student.name} Failed!", students))
print(map_results)


########## EXERCISE:
                    #Use map to multipy all numbers by 2:


numbers = [1,2,3,4,5,6]

                # map(lambda parameter: parameter * 2, from list[numbers])
multipys = list(map(lambda numb: numb * 2, numbers))
print(multipys)
