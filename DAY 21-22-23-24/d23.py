"""
polymorphism

Polymorphism ->
The word "Polymorphism" means many forms.
In Python, polymorphism allows the same  method,
operator, or funnction name to have different behaviors,
depending on the object or context.

Why use polymorphism?

1. Makes code flexible and dynamic.
2. Supports the concept of generalization.
3. Improves readability and reuseability.
4. Helps in implementing real world behavior


Types of Polymorphism in Python
1. Method Overriding - Child class redefines parent class method.
2. Method Overloading -Same method with different parameters.
3. Operator Overloading - Same operator behaves differently for different
objects.

Real -Life Example Analysis:

Imagine a Payment system. The method "pay()" can behave differently.
> For credit card - pay() deducts from bank
> For paypal - pay() uses wallet
> For Crypto - pay() uses blockchain
This polymorphism in action.

==============================================================================
"""

print("\n==============================")
print("  Basic 5 Polymorphism Examples")
print("==============================")

# Example 1: Function Polymorphism [ built -in function 'len']

print("Length of String:",len("Shalini"))
print("Length of list",len([10,20,30]))
print("Length of Dictionary:",len({'a':1,"b":2}))

# Example 2: Method Overriding
class Bird:
    def sound(self):
        print('Birds make sound')
        
class Sparrow(Bird):
    def sound(self):
        print("Sparrow Chirps.")
        
class Parrot(Bird):
    def sound(self):
        print("Parrot talks.")
        
birds =[ Sparrow(),Parrot()]
for b in birds:
    b.sound()
    
    
# Example 3: Operator Overloading
# '+' is redefined to add pages of two book objects.

class Book:
    def __init__(self,pages):
        self.pages = pages
        
    def __add__(self,other):
        return self.pages+other.pages

b1 = Book(100)
B2 = Book(200)
print("Total Pages in 2 Books :",b1+B2)


# Example 4: Method Overloading using default arguements
# same func add works for 2 or 3 arguements
def add(a,b=0,c=0):
    return a+b+c

print(f"Add two numbers : {add(5,10)}")
print(f"Add three numbers : {add(5,10,20)}")

# Example 5: Polymorphism in different classes
class Circle:
    def __init__(self,r):
        self.r=r
        
    def area(self):
        return 3.14*(self.r**2)
    
class Square:
    def __init__(self,s):
        self.s=s
        
    def area(self):
        return self.s*self.s
    
shapes =[ Circle(5),Square(4)]
for s in shapes:
    print("Area: " ,s.area())


print("\n==============================")
print("  5 Examples: Method Overriding")
print("==============================")

# 1. Animal Sounds
class Animal:
    def speak(self):
        print("Animal Speaks")
        
class Dog(Animal):
    def speak(self):
        print("Dog Barks !")
        
class Cat(Animal):
    def speak(self):
        print("Cat meows.")
        
for s in [Dog(),Cat()]:
    s.speak()
    
#2. Employee Salary Calculation
class Employee:
    def salary(self):
        print("Base Salary")
        
class Manager(Employee):
    def salary(self):
        print("Base Salary "+"Bonus")
        
class Developer(Employee):
    def salary(self):
        print("Base Salary "+"Incentives")
        
for e in [Manager(),Developer()]:
    e.salary()
    
# 3. Vehicle Speed
class Vehicle:
    def speed(self):
        print("Generic vehicle Speed")

class Car(Vehicle):
    def speed(self):
        print("Car speed: 120 km/hr")
        
class Bike(Vehicle):
    def speed(self):
        print("Bike Speed: 80 km/hr")
        
for v in [Car(),Bike()]:
    v.speed() 
    

# 4. Payment Modes
class Payment:
    def pay(self):
        print("Generic payment")
        
class CreditCard(Payment):
    def pay(self):
        print("Paid via Credit Card")
        
class Paypal(Payment):
    def pay(self):
        print("PAID VIA PAYPAL")
        
for p in [CreditCard(),Paypal()]:
    p.pay()
     
     
# 5. University Roles

class Person:
    def role(self):
        print("General Person")

class Student(Person):
    def role(self):
        print("Student attends class")

class Teacher(Person):
    def role(self):
        print("Teacher delivers lectures")
        

for person in [Student(),Teacher()]:
    person.role()
    
    
"""
METHOD OVERLOADING
[ Not supported in Python]

"""
def multiply(a,b=1,c=1):
    return a*b*c

print("Multiply 2 numbers :",multiply(2,3))
print("Multiply 3 numbers :",multiply(2,3,4))

# remaining examples in practice

# Operator Overloading
class Complex:
    def __init__(self,x,y):
        self.x,self.y=x,y
        
    # Overloading
    def __add__(self,other):
        return Complex(self.x+other.x,self.y+other.y)
    
    # overloadinng print
    def __str__(self):
        return f"{self.x}+{self.y}"
    
c1,c2 = Complex(2,3),Complex(1,4)
print("Sum",c1+c2)

"""
Encapsulation

Encapsulation -->
Encapsulation is the process of wrapping data (variables) and methods
(functions) into a single unit ( class )

It restricts direct access to variables and prevents accidental modification,
ensuring data security.

Access Specifiers in Python:

1. Public Member -> Accessible everywhere ( default).
2. Protected Member -> Accessible inside class and subclasses [_variable]
3. Private Member -> Accsessible only inside class [__variable]

Why use Encapsulation ?
1. Data security and control
2. Hides implementation details
3. Increases modularity and maintainability
4. Prevents unintended interference

Real- Life Example Analysis:

Think of a Bank Account:
- Balance should not be accessed directly.
- Only controlled actions like deposit() or withdrw() should modify it.
This is encapsulation in action


"""

# Example 1 : Public Members
class Student:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        
    def display(self):
        print(f"Student : {self.name}, Age : {self.age}")

s = Student('Rahul',21)
s.display()
print("Accessing Public Variable",s.name) 


# Example 2: Protected Members

class Employee:
    def __init__(self,name,salary):
        self._name = name
        self._salary = salary
        
    def show(self):
        print(f"Employee : {self._name},Salary:{self._salary}")
        

class Manager(Employee):
    def manage(self):
        print(f"Manager {self._name} manages with salary {self._salary}")
        

m = Manager('Shalini',90000)
m.show()
m.manage()

    
    
