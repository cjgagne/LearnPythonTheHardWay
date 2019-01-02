## Animal is an object (yes, sort of confusing) look at the extra credit
class Animal(object):

    def __init__(self, sound):
        self.sound = sound


## Dog is an Animal
class Dog(Animal):
 
    def __init__(self, name, sound):
        ## Dog has a name
        super(Dog, self).__init__(sound)
        self.name = name


## Cat is an Animal
class Cat(Animal):
    
    def __init__(self, name, sound = "Meow"):
        ## Cat has a name
        super(Cat, self).__init__(sound)
        self.name = name

## Person is an object
class Person(object):

    def __init__(self, name):
        ## Person has a name
        self.name = name

        ## Person has a pet of some kind
        self.pet = None


## Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee is a Person that has a name
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## Salmon is a Fish
class Salmon(Fish):
    pass

##Halibut is a Fish
class Halibut(Fish):
    pass


## Rover is a Dog
rover = Dog("Rover", "Arf")
print(rover.sound)

## Satan us a Cat
satan = Cat("Satan")
print(satan.sound)

## Mary is a Person
mary = Person("Mary")

## Mary is a Person with a pet Cat named Satan
mary.pet = satan

## Frank is an Employee with name Frank and salary $120,000
frank = Employee("Frank", 120000)

## Frank is a Person with a Pet
frank.pet = rover

## Flipper is a Fish
flipper = Fish()

## Crouse is a Salmon
crouse = Salmon()

## Harry is a Halibut
harry = Halibut()
