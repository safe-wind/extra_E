#es 7 functions - pynative.com

#Below is the function display_student(name, age).
#  Assign a new name show_tudent(name, age) to it
#  and call it using the new name.

def displayStudent(name:str, age:int) -> None:

    print(name, age)

def showStudent(**args):
    print(*args)


showStudent == displayStudent("Mario", 23) 

showStudent()
