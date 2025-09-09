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

"""
Types of Constructors in Python: Unlike Java/C++ , Python officially supports
only one constructor (__init__), but we can categorize them as:

1. Default Constructor
No parameters (except self).
Initializes with fixed/default values.

Example:
"""
class Student:   # default constructor
    def __init__(self):
        self.name ='Unknown'
        self.age = 18
s1 = Student()
print(s1.name,s1.age)

"""
2. Parameterized Constructor
Takes arguements to initialize attributes dynamically

Example
"""
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age =age
        
s1 = Student('Amit',20)
print(s1.name,s1.age)

"""
3. Copy Constructor(Not Built-in,but created manually)
Used to create a new object as a copy of another object.
Python don't have an inbuilt copy constructor like C__,
but we can implement it overselves.

Example
"""
class Student:
    def __init__(self,name,age):
        self.name =name
        self.age = age
        
    # copy constructor
    @classmethod
    def copy(cls,obj):
        return cls(obj.name,obj.age)
    
s1 =Student('Riya',21)
s2 = Student.copy(s1)
print(s2.name,s2.age)

# 6. Laptop Example
class Laptop:
    def __init__(self,brand,ram,storage,os,price):
        self.brand =brand
        self.ram = ram
        self.storage = storage
        self.os =os
        self.price =price
        
    def upgrade_ram(self,extra):
        self.ram +=extra
        print(f"{self.brand} RAM upgraded to {self.ram} GB")
        
    def show_specs(self):
        print(f"{self.brand} LAPTOP-> RAM: {self.ram} GB, Storage :{self.storage}, OS : {self.os} , Price : {self.price}")
        
        
lap1 = Laptop('Dell',8,512,'Windows11',55000)
lap1.show_specs()
lap1.upgrade_ram(4)
lap2 = Laptop('Apple',16,1024,'macos',120000)
lap2.show_specs()
lap2.upgrade_ram(8)


# 7. Teacher Examples
class Teacher:
    def __init__(self,name,subject,exp,emp_id,salary):
        self.name =name
        self.subject = subject
        self.exp = exp
        self.emp_id = emp_id
        self.salary = salary
        
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")
        
    def increment_salary(self,amount):
        self.salary +=amount
        print(f"{self.name}'s new salary is {self.salary}")
        
        
t1 = Teacher('Meena','Maths',10,301,40000)
t1.teach()
t1.increment_salary(5000)

t2 = Teacher('Rajesh','English',8,302,35000)
t2.teach()
t2.increment_salary(7000)


# 8. Dog Example
class Dog:
    def __init__(self,name,breed,age,color,owner):
        self.name =name
        self.breed = breed
        self.age = age
        self.color =color
        self.owner = owner
        
    def bark(self):
        print(f"{self.name} ({self.breed}) says Woof!")
        
    def showinfo(self):
        print(f"Dog : {self.name}, Breed: {self.breed}, Age: {self.age}, Color: {self.color}, Owner :{self.owner}")
        
        
d1 = Dog('Tommy','Labrador',3,'Golden','Amit')
d2 = Dog('Sheru','German Shpherd',4,'Black','Priya')
d1.bark()
d2.bark()
d2.showinfo()
d1.showinfo()

# 9. Resturant Example 
class Resturant:
    def __init__(self,name,location,rating,cuisine,owner):
        self.name = name
        self.location = location
        self.rating = rating
        self.cuisine = cuisine
        self.owner = owner
        self.menu ={}
        
    def add_item(self,item,price):
        self.menu[item]=price
        print(f"{item} added to {self.name} menu")
    
    def show_menu(self):
        print(f'{self.name} ({self.cuisine}) Menu : {self.menu}')
        
        
r1 = Resturant('Foodies Hub','Delhi',4.5,'Indian','Sunita')
r1.add_item('Paneer Tikka',250)
r1.show_menu()

r2 = Resturant('Pizza World','Mumbai',4.2,'Italian','Rakesh')
r2.add_item('Margherita Pizza',300)
r2.show_menu()


# 10. Shopping Cart Example
class ShoppingCart:
    def __init__(self,user,date,store,cart_id,location):
        self.user = user
        self.date = date
        self.store = store
        self.cart_id = cart_id
        self.location = location
        self.items = []
        
    def add_items(self,item):
        self.items.append(item)
        
    def show_cart(self):
        print(f"Cart {self.cart_id} ({self.user}) Items : {self.items}")
        
        
c1 = ShoppingCart('Anil','2025-08-26','Amazon',101,'Delhi')
c1.add_items('Laptop')
c1.show_cart()
c2 = ShoppingCart('Sonia','2025-08-26','Flipkart',102,'Mumbai')
c2.add_items('Shoes')
c2.show_cart()

# 11. Phone Example
class Phone:
    def __init__(self,brand,number,model,os,price):
        self.brand =brand
        self.number = number
        self.model = model
        self.os = os
        self.price = price
    
    def call(self,other_number):
        print(f" {self.brand} {self.model} calling {other_number} from {self.number}")
    
    def show_info(self):
        print(f"Phone : {self.brand} {self.model} , OS : {self.os} ,Price :{self.price}")
        
        
p1 = Phone('Samsung','9221836894','Galaxy S20+','Xelenx',5000)
p1.show_info()
p1.call('9702626407')


# 12 School Example
class School:
    def __init__(self,name,location,board,principal,established_year):
        self.name = name
        self.location = location
        self.board = board
        self.principal = principal
        self.established_year = established_year
        self.students =[]
    
    def add_student(self,student_name):
        self.students.append(student_name)
        print(f"{student_name} admitted to {self.name}")
    
    def show_students(self):
        print(f"Students in {self.name} : {self.students}")

    
school1 = School('Green Valley School','Delhi','CBSE','Mr. Sharma',1995)
school1.add_student('Ravi')
school1.show_students()
school1.add_student('Sneha');school1.show_students()

# 13. Movie Example
class Movie:
    def __init__(self,title,duration,genre,director,release_year):
        self.title = title
        self.duration = duration
        self.genre = genre
        self.director = director
        self.release_year = release_year
        
    def play(self):
        print(f"Playing movie : {self.title} ({self.duration} mins)")
        
    def show_info(self):
        print(f"{self.title} | Genre : {self.genre} , Director : {self.director} , Year : {self.release_year} ")
        
        
m1 = Movie('Inception',148,'Sci-Fi','Christographer Nolan',2010)
m1.play()
m1.show_info()

m2 = Movie('3 Idiots',170,'Comedy-Drama','Rajukmar Hirani',2009)
m2.show_info()
m2.play()


# 14. Hospital Example 
class Hospital:
    def __init__(self,name,location,type,capacity,established):
        self.name = name
        self.location = location
        self.type = type
        self.capacity = capacity
        self.established = established
        self.patients = []
        
        
    
    def admit_patient(self,patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            print(f"{patient} admitted to {self.name}")
        else:
            print('No beds available')
            
    
    def show_patients(self):
        print(f"Patients in {self.name} : {self.patients}")
        
        
Hospital1 = Hospital('City Hospital','Delhi','Multi-Speciality',2,1990)
Hospital1.admit_patient('Ramesh')
Hospital1.show_patients()

Hospital2 = Hospital('Apollo','Navi Mumbai','Private',3,2001)
Hospital2.admit_patient('Sita')
Hospital2.show_patients()

# 15. Train Example
class Train:
    def __init__(self,train_no,name,source,destination,seats):
        self.train_no = train_no
        self.name = name
        self.source = source
        self.destination = destination
        self.seats = seats
        
    def book_seats(self):
        if self.seats >0:
            self.seats -=1
            print(f"Ticket booked in {self.name}. Remaining seats : {self.seats}")
            
    
    def show_info(self):
        print(f"Train {self.train_no} - {self.name} from {self.source} to {self.destination}")
        
       
tr1 = Train(10101,'Rajdhani Express','Delhi','Mumbai',2)
tr1.book_seats()
tr1.show_info()

tr2 = Train(10102,'Shatabdi Express','Delhi','Chandigarh',1 )
tr2.show_info()
tr2.book_seats()

# 16. University Class Example
class University:
    def __init__(self,name,location,students):
        self.name = name
        self.location = location
        self.students = students
    
    def enroll_students(self,number):
        self.students +=number
        print(f"{number} students enrolled. Total now : {self.students}")
        
    def conduct_exam(self):
        print(f"{self.name} is conducting semester exams for {self.students} students")
        
        
uni1 = University('Harvard Universtiy','USA',20000)
uni1.enroll_students(500)
uni1.conduct_exam()

# 17,18,19 remaining 

"""
Purpose of Learning OOPS Concepts in Python

1. Reuseability - Write once reuse many times

2. Modularity - Break work into smaller pieces

3. Maintainability - Easy to change or fix

4. Scalability - Grow to large systems naturally

5. Real World Mapping - Model Natural Entities

6. Data Encapsulation - Protect and validate data

7. Inheritance - Build on existing classes

8. Polymorphism - Same method name, Different behaviors

9. Abstraction - Hide internals, show an interface

10. Code REUSE Accross Projects - Ship faster consistently 


"""