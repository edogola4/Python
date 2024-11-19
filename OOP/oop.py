## OOP

'''
Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.
Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
'''

# Let's start with designing a class representing a Smartphone.
# The class will have attributes like brand, model, battery_percentage, and is_on to represent the state of the smartphone.
# We'll also define methods such as turn_on(), turn_off(), charge(), and use_phone() to interact with the smartphone.
# The class will also have a constructor (__init__) to initialize these attributes.

class Smartphone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is now turned on.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} {self.model} is now turned off.")

    def charge(self, charge_percentage):
        self.battery_percentage = min(100, self.battery_percentage + charge_percentage)
        print(f"{self.brand} {self.model} is now charged to {self.battery_percentage}%.")

    def use_phone(self):
        if self.is_on:
            print(f"{self.brand} {self.model} is being used.")
        else:
            print(f"{self.brand} {self.model} is turned off. Please turn it on first.")

# Now, let's create instances of the Smartphone class and interact with them.
# We'll create two instances: my_smartphone and my_friend_smartphone.

my_smartphone = Smartphone("Samsung", "Galaxy S21", 80)
my_friend_smartphone = Smartphone("iPhone", "iPhone 13", 70)

# Let's turn on my smartphone and use it.
my_smartphone.turn_on()
my_smartphone.use_phone()

# Let's charge my smartphone.
my_smartphone.charge(20)

# Let's turn off my smartphone.
my_smartphone.turn_off()

# Let's turn on my friend's smartphone and use it.
my_friend_smartphone.turn_on()
my_friend_smartphone.use_phone()

# Let's charge my friend's smartphone.
my_friend_smartphone.charge(30)

# Let's turn off my friend's smartphone.
my_friend_smartphone.turn_off()


# Using the methods
my_smartphone.turn_on()
my_smartphone.use_phone()
my_smartphone.charge(20)
my_smartphone.turn_off()
my_smartphone.use_phone()
my_friend_smartphone.turn_on()
my_friend_smartphone.use_phone()
my_friend_smartphone.charge(30)
my_friend_smartphone.turn_off()
my_friend_smartphone.use_phone()

'''
Explanation:
Attributes: brand, model, battery_percentage, and is_on.
Methods:
turn_on() and turn_off() change the power state of the phone.
charge() sets the battery percentage to 100%.
use_phone() decreases the battery percentage based on the number of hours the phone is used.
'''






## Polymorphism Challenge! 🎭
# create two classes: Car and Plane, both having a method move() but with different behaviors. 
# This demonstrates polymorphism where the method name remains the same, but its implementation differs across classes.

class Car:
    def move(self):
        print("Driving 🚗")


class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚢")

        # creating class indtances

car = Car()
plane = Plane()
boat = Boat()

# demonstrating polymorphism

vehicles = [car, plane, boat]

for vehicle in vehicles:
    vehicle.move() # each object calls its own method of move
    print("----")
'''
Explanation:
Each class (Car, Plane, Boat) has its own implementation of the move() method.
When we iterate over the list vehicles, each object invokes its own version of the move() method, demonstrating polymorphism.
In this way, you can see how different objects can share a common interface (the move() method) but implement different behaviors depending on their class.
'''


