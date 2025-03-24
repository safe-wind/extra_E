# Given is the class Animal. For each task, test your changes!
# 1. Create two realistic instances of Animals
# 2. Print the name of each object
# 3. Change the amount of legs of one object using the dot notation
# 4. Add a method setLegs() to set the legs of an object and repeat task 3 but
#    this time using the method.
# 5. Add a method getLegs() to return the amount of legs
# 6. Add a method named printInfo that prints all attributes of the Animal
            

class Animal:

    def __init__(self, name:str, num_legs:int):

        self.name = name
        self.num_legs = num_legs
        

    def setLegs(self, new_legs:int) -> int:
        
        self.num_legs = new_legs
        return self.num_legs
    
    def getLegs(self) -> None:
        print(self.num_legs)

    def displayInfo(self) -> None:
        print(f"Name: {self.name}\nNum. of legs: {self.num_legs}")



a1 = Animal("cat", 4)


a2 = Animal("Dog", 4)
a2.setLegs(3)

a2.displayInfo()

a3 = Animal("whale", 0)
a3.displayInfo()



