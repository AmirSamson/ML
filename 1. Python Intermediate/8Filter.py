class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score 
                                # repr is an abbriation for `represent`
    def __repr__(self):             # whenever this is called, it is going to print the ``` f"{self.name}: {self.score}" ```
        return f"{self.name}: {self.score}"
               
students = [student("Amir", 0.12), student("Ali", 0.14), student("Samson", 0.19), student("Milad", 0.20), student("Hesam", 0.15)] 

failing_students = []
for student in students:
    if student.score < 0.15:
        failing_students.append(student)

                                    #### we can filter our list with the following method: 

filter_list = list(filter(lambda student: student.score < 0.15, students))    # This will filter the failed students out of our list.

print(filter_list)

                ### Notice this in the response "return f"{self.name}: {self.score}"" ??  it is in the   `` def __repr__(self) ``
                ### This is how it will represent the data in the list when we print the list.

###### Challenge: 

# use filter to list out all the even numbers:

numbers = [1,2,3,4,5,6,7,8,9]

        ## The "% 2 == 0" is going to filter the even numbers which they can be devided by 2 and have 0 remainder (باقی مانده):
print(list(filter(lambda even: even %2 == 0, numbers)))

              ## But if we only use the "% 2" we will have all the odd numbers ===> ``` [1, 3, 5, 7, 9] ```