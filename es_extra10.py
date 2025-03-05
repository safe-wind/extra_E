#es 4 functions (pynative.com)

#Write a program to create a function show_employee()
#using the following conditions.
#It should accept the employee’s name 
#and salary and display both.
#If the salary is missing in the function
#call then assign default value 9000 to salary

def showEmployee(par1:str, par2= 9000) -> None:

    print(f"Name: {par1}, salary: {par2}$")

showEmployee("Gianni")
showEmployee("Sara", 9500)
