class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score 
                                # repr is an abbriation for `represent`
    def __repr__(self):             # whenever this is called, it is going to print the ``` f"{self.name}: {self.score}" ```
        return f"{self.name}: {self.score}"
               
students = [student("Amir", 0.12), student("Ali", 0.14), student("Samson", 0.19), student("Milad", 0.20), student("Hesam", 0.15)] 

# failing_students = []

score_total = 0
for student in students:
    score_total += student.score  ## it will take the "score_total" and adds it to "student.score with +="

print(score_total / len(students))


##### How to use reduce: 

from functools import reduce
                                                          # starting value is 0
reduce_total = reduce(lambda total, student: student.score + total, students, 0)

print(reduce_total / len(students))







###### Challenge: 

# use filter to list out all the even numbers:

numbers = [1,2,3,4,5,6]

from functools import reduce

print((reduce(lambda total, multipy: multipy * total, numbers, 1)))

### or we can use: 

print(reduce(lambda total, mult: mult * total, numbers))   ### since here the list is all number. but previous list had student names and etc.

             
