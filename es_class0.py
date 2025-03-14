
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
luca = Person("Luca L.", 35)
sara = Person("Sara F.", 24)
sofia =Person("Sofia S.", 27)

print(alice.age)

if alice.age > bob.age:
    print(alice.name)
else:
    print(bob.name)

people:list[Person] = [alice, bob, luca, sara, sofia]

youngest = people[0]

for persona in people:

    if persona.age < youngest.age:
        
        youngest = persona
        
print(youngest.name)

