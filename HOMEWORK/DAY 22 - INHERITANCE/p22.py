"""
OOPS- INHERITANCE 
PRACTICE THING

"""

# 1. Single Inheritance 

# Example 2 : Vehicle -> Car
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
        
    def move(self):
        print(f"{self.brand} vehicle is moving")
        
class Car(Vehicle):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model = model
        
    def info(self):
        print(f" Car info : {self.brand} {self.model}")
        
car = Car('Toyota','Camry')
car.move()
car.info()

        
# Example 3: Person -> Student
class Person:
    def __init__(self,name):
        self.name = name
    
    def introduce(self):
        print(f"My name is {self.name}")
        
class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")
        

Student = Student('Rahul')
Student.introduce();Student.study()


# Example 4 : Device -> Laptop
class Device:
    def __init__(self,name):
        self.name =name
        
    def power_on(self):
        print(f"{self.name} is now ON.")
        
class Laptop(Device):
    def code(self):
        print(f"{self.name} is used for coding")
    
    
lappy = Laptop('Dell')
lappy.power_on()
lappy.code()


# Example 5: Employee -> Manager
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def details(self):
        print(f"Employee : {self.name},Salary : {self.salary}")
        
class Manager(Employee):
    def manage(self):
        print(f"Manager {self.name} is managing the team")
        

mgr = Manager('Shalini',90000)
mgr.details()
mgr.manage()

"""
2. Multiple - Inheritance

"""

# Example 2 : Teacher + Coach -> Student
class Teacher:
    def teach(self):
        print(f"Teacher is teaching.")
        
class Coach:
    def train(self):
        print('Coach is training sports')
        
class Student(Teacher,Coach):
    def perform(self):
        print('Student is performing well')
        
        
s= Student()
s.teach()
s.train()
s.perform()

# Example 3: Engine + Body -> Car
class Engine:
    def engine_type(self):
        print('Engine : V8 Petrol')

class Body:
    def design(self):
        print('Body : Sedan')
        

class Sports_Car(Engine,Body):
    def info(self):
        print(f"Sports Car is Powerful and Stylish.")
        
        
sc = Sports_Car()
sc.engine_type()
sc.design()
sc.info()


# Example 4: Keyboard = Screen -> Laptop
class Keyboard:
    def input_device(self):
        print("Keyboard is used for typing")

class Screen:
    def display(self):
        print('Screen : Displays visuals.')

class Laptop(Keyboard,Screen):
    def work(self):
        print('Laptop : Combination of input and output devices')
        
        
lap = Laptop()
lap.input_device()
lap.display()
lap.work()


# Example 5: Musician + Writer -> Artist
class Musician:
    def play_music(self):
        print('Musician plays Guitar')
        
class Writer:
    def write(self):
        print('Writer writes poetry.')
        
class Artist(Musician,Writer):
    def show(self):
        print('Artist Shows creativity.')
        
        
artist = Artist()
artist.play_music()
artist.write()
artist.show()

