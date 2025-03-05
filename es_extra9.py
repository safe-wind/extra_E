#es functions (pynative.com)

#Write a program to create function 
#calculation() such that it can accept 
#two variables and calculate addition 
#and subtraction. Also, it must return 
#both addition and subtraction in 
#a single return call.

def calculation(arg1:int, arg2:int) -> int:

    result_add: int = arg1 + arg2
    result_sub: int = arg1 - arg2

    return result_add, result_sub

print(calculation(20, 10))
