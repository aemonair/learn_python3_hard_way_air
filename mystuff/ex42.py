## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal (object):
    pass

## has-a
class Dog(Animal):
    def __init__(self, name):
        ## ?? 
        self.name = name

## has-a
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## has-a
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## has-a
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## has-a
class Fish(object):
    pass

## has-a
class Salmon(Fish):
    pass

## has-a
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## is-a
mary.pet = satan

## is-a
frank = Employee("Frank", 120000)

## is-a
frank.pet = rover

## is-a
flipper = Fish()

## is-a
crouse = Salmon()

## is-a
harry = Halibut()
