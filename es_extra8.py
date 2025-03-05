#es 2 function (pynative.com)
#Write a program to create function func1() to accept a variable length of arguments and print their value.

#Note:
#Create a function in such a way that we can 
#pass any number of arguments to this function,
#and the function should process them and 
#display each argument’s value.

def varArgument(*args:int) -> None:

    for x in args:

        print(x)

varArgument(10, 20, 30, 55)