## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## A Dog is-a an animal
class Dog(Animal):

    def __init__(self, name):
        ## A Dog has-a name
        self.name = name

## A Cat is-an animal
class Cat(Animal):

    def __init__(self, name):
        ## A Cat has-a name
        self.name = name

## A Person is-an Object
class Person(object):

    def __init__(self, name):
        ## A Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet called satan
mary.pet = satan

## employee frank has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet called rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is-a salon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()
