"""
What is Object Oriented Programming ?

Objected Oriented Programming [OOPS] is a programming paradigm that 
organises code into objects, which represent real-world entities.

Each object contains:
--> Properties [Data/Variable] ->Describe the object
--> Behaviors [Methods/Functions ] -> actions the object can perform

Note: OOP allows modularity,reuseability,scalability and cleaner project structures.
It is heavily used in software development, data analysis, machine learning, and
web applications.

4 pillars of OOPS:
1. Inheritance - Build on existing classes
2. Polymorphism - Same method name, different behaviours
3. Abstraction -Hide internals, show an interface
4. Data Encapsulation - Protect and validate data


Class: Class is a blueprint/template used to create objects. It defines
      properties [attributes] and behaviours [methods].
      
      
Example : Person,Employee,Bank,etc......

Important Points:
1. Defined using the class keyword.
2. Attributes -> Variables inside a class
3. Methods -> Functions inside a class
4. A class itself does not hold data -> objects store actual values.


Syntax :
class ClassName:
      #code

Object:
An object is an instance of a class. Each object has its own state [attributes] and
behaviour [methods ].

Example : Dog, Chair, Laptop,etc......

Important Points:
1. Created from a class.
2. Each object has its own copy of attributes
3. Multiple objects can be created from one class.

Syntax:
object_name =ClassName(arguements)

constructors:
A constructor (__init__) is a special function that is automatically called when
a new object is created.

Important Points:
1. Always named __init__.
Used to initialize attributes.
Runs only once when the object is created.

Syntax:
class Classname:
def __init__(self,arg1,arg2):
        self.attr1=arg1
        self.attr2.arg2
        
        
What is a self in Constructor ?
-> Self ia a reference to the current object.
-> It allows you to access the variables and methods inside the class.
--> Every instance (object) passes itself as the first arguement 
automatically.

Example: self.brand are self.car are different for each object
"""

class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color = color
        
c1= Car('BMW','Black')
c2 = Car('Audi','Red')

print(c1.brand,c1.color)
print(c2.brand,c2.color)

"""
Functions/Methods:
Methods are functions inside a class that define the behavior of objects.

Example: start(),run(),post()

Important Points:
1. Always have self as the first parameter -> refers to the current object
2. Can modify attributes of the object.
3. Type: Instance methods, class methods, static methods


Syntax:
class ClassName:
    def methods_name(self,args):
        # code
        
        
Instead of writing code in a linear way, OOP allows us to structure programs
like the real world:

1. Car -> has properites like color, model, speed and behaviors like
start(), stop(), accelerate().
2. Student -> has properties like name, age, marks and behaviors like study(), give_exams()
3. Bank Account -> has properties like account_number,balance and behaviors like deposit(),
withdraw(), check_balance()
4. Employee -> has properties like name,position, salary and behaviors like work(), get_salary(),
promote()
5. Book _> has properites like title, author, availability_status and behaviors like
borrow(),return_book()
"""

# Real World Examples in Python
# Classes, Objects, Constructors, Variables and Functions

#1. Car Example:
class Car:
    def __init__(self,color,model,speed,fuel,owner):
        self.color=color
        self.model = model
        self.speed= speed
        self.fuel =fuel
        self.owner= owner
        
    
    def start(self):
        print(f"{self.model} owned by {self.owner} started")
        
    def accelerate(self):
        self.speed +=10
        print(f"{self.model} speed increased to {self.speed} km/hr")
        
    
car1 =Car('Red','Honda Civic',60,'Petrol','Alice')
car1.start()
car1.accelerate()

car2 = Car('Blue','Toyoto Corolla',50,'Diesel','Bob')
car2.start()
car2.accelerate()
        
# 2. Student Example 
class Student:
    def __init__(self,name,age,marks,course,roll_no):
        self.name = name 
        self.age = age 
        self.marks =marks 
        self.course = course 
        self.roll_no= roll_no
        
    def study(self):
        print(f"{self.name} is studying {self.course}")
    
    def give_exam(self):
        print(f"{self.name} scored {self.marks} marks in the exam")
        
    
s1 = Student('Ravi',20,88,'BBA',101)
s1.study()
s1.give_exam()

s2 = Student('Sneha',21,92,'BCA',102)
s2.study()
s2.give_exam()

# 3. Bank Account Example
class BankAccount:
    def __init__(self,acc_num,balance,holder,branch,bank_name):
        self.acc_num =acc_num
        self.balance = balance
        self.holder =holder
        self.branch =branch
        self.bank_name =bank_name
        
    def deposit(self,amount):
        self.balance +=amount
        print(f"{self.holder} deposited {amount}. Balance ={self.balance}")
        
    
    def withdraw(self,amount):
        print(self.balance,amount)
        if amount<=self.balance:
            self.balance -= amount
            print(self.balance)
            print(f"{self.holder} withdrew {amount}. Balance = {self.balance}")
        else:
            print("Insufficient Funds")
            
# self,acc_num,balance,holder,branch,bank_name):
acc1 =BankAccount(1001,5000,'Rohit','Delhi','Sbi')
acc2 = BankAccount(1002,8000,'Anita','Mumbai','HDFC')
acc1.deposit(5000)
acc1.withdraw(100)


# 4. Employee Example
class Employee:
    def __init__(self,name,position,salary,emp_id,department):
        self.name =name
        self.position =position
        self.salary =salary
        self.emp_id =emp_id
        self.department =department
          
    def work(self):
        print(f"{self.name} is working in {self.department} department")
    
    def promote(self,amount):
        self.salary +=amount
        print(f"{self.name} promoted! New Salary: {self.salary}")
        

e1 =Employee('Vikram','Manager',50000,201,'HR')
e1.salary
e1.work()
e1.promote(8000)

e2 = Employee('Kiran','Developer',40000,202,'IT')
e2.work()
e2.promote(5000)


#5. Book Example
class Book:
    def __init__(self,title,author,genre,year,pages):
        self.title =title
        self.author = author
        self.genre = genre
        self.year = year
        self.pages =pages
        self.available = True
        
    def borrow(self):
        if self.available:
            self.available =False
            print(f"{self.title} is borrowed")
        else:
            print(f"{self.title} is not available")
            
    
    def return_book(self):
        self.available =True
        print(f"{self.title} is returned")


b1 =Book('Python Basics','Guido','Education',2020,350)
b1.borrow()
b1.return_book()

b2 = Book('AI Future','John','Technology',2022,280)
b2.borrow()
b2.return_book()



    

