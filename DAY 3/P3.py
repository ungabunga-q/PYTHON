"""
Practice Set
"""
""" # print 
print("Hello World!")
print("Welcome to Python class")

# input

age = int(input("Enter your age"))
print(f"Age is {age}")

year = int(input('Which year it is going on?'))
print(f"Year is {year}")

#type conversion
age = 27
print("Type age: ",type(age))
print("Type age decimal",type(float(age)))


#variable
pet = "dog"
pet1 = "cat"
print(pet,pet1)
 """

# Today's Work

# Calculate total marks of students ; Subjects :Hindi, English, Maths, History, Arts
# Marks of Hindi, English, Maths, History, Arts 
hindi = int(input("Enter marks in Hindi"))
english = int(input("Enter marks in English"))
maths = int(input("Enter marks in Maths"))
history = int(input("Enter marks in History"))
arts = int(input("Enter marks in Arts"))

total_score = hindi+english+maths +history + arts
print(total_score)

# average hotel rating
a1 = float(input("Enter hotel rating: "))
a2 = float(input("Enter hotel rating: "))
a3 = float(input("Enter hotel rating: "))
a4 = float(input("Enter hotel rating: "))
a5 = float(input("Enter hotel rating: "))
a_total = (a1+a2+a3+a4+a5)/5
print(f"Average rating of hotel is {a_total}") 
"""

Remember to use int() and float() while working with numbers 
The input() function always returns a string, so you need to convert it to a number
if you want to peform mathematical operations on it.
"""

""" 
# without conversion
a= input("Enter number")
b = input("Enter another number")

print(a+b) # concatenates

# With Conversion
a= int(input())
b = int(input())
print(a+b) #adds

# ===========================================================
# GREET THE USER
#==================================================================

# input() ------------------------->> Used to take input from the user

name = input("Enter your name: ")
print(f"Welcome , {name}") # f strings

age = input('Enter your age?')
print(f"Hello, {name} you are {age} years old") # f strings

print("*"*50)

#==============================
# VARIABLES """
#==================================
"""
A variable is a named container to store data.
Python is dynamically typed. No need to declare data types.

"""
# Syntax:
# variable_name = value
name =123
name ="Hello"

# Examples:
name = "Shalini"
age = 28
city= "MUMBAI"
Fees = 5000.75
is_available = True
temperature = 37.5
mobile ="9221837654"

#====================================
# DATA TYPES
#=====================================
"""_
Python supports the following data types:
1. int - Integer ( eg -10)
2. float - Decimal Numbers  ( eg - 5.67)
3. str - String , Text Data( eg - "Hello")
4. bool - Boolean ( eg - True/False)
5. list - Ordered collection of items ( eg - [1,2,3]), allow duplicates
6. tuple - Ordered collection of items ( eg - (1,2,3)),allow duplicates, cannot change 
7. dict - Unordered collection of key-value pairs ( eg - {"name":"Shalini
8. set - Unordered collection of unique items ( eg - {1,2,3}),no duplicates
9. complex - Complex numbers ( eg - 3+4j)
10. NoneType - Represents no value
"""

# Real WORLD Examples:
units = 10               #int
price =99.99             #float
product = "Laptop"       #string
is_active = True         #bool
items =["pen","book"]     #list
dimensions = (20,15,10)   #tuple
unique_ids ={101,103}     #set
student ={"name":"Shalini","age":22}  #dict
data = None

#Type Checking
print(type(units))


print("*"*50)
print("Operators in Python")
print("*"*50)
"""
Operators are used to perform operations on variables and values.
Types:
1. Arithmetic:
2. Relational ( Comparision)
3. Logical
4. Assignment
5. Membership
6. Identity
7. Bitwise
    """
#=========
# +,-,*,/,%,**,//
a=15
b=4
print(a+b) #addition
print(a-b) #substraction
print(a*b) #multiplication
print(a/b) #division
print(b**2) #exponent
print(a//b) #floor division
print(a%b) #modulus

# Real life:
price =50
quantity = 3
print("Total: ",price*quantity)

marks = (80+70+50)/3
print("Average: ",marks)

seconds = 250
print("Minutes :",seconds//60)

#=========
#2. RELATIONAL OPERATORS
# ==,!=,>,<,>=,<=

age = 20
print(age>18)   #True

marks = 45
print(marks >=40) #True

amount = 999
print(amount < 1000 )  #False

entered_pin = 1234
real_pin = 4321
print(entered_pin==real_pin)  #False

temp = 25
print(temp != 30) #True

height = 154
print(height > 150)

weight = 65
print(weight <=70) # True

name ="Aishwarya"
print(name=="Aishwarya")

price = 200
print(price >=100 and price <=500)

num = 6
print(num %2==0)

# ==================================
# 3. ASSIGNMENT OPERATORS
# =, +=, -=, *=, /=, %=, **=, //=
# 
"""
x = 10
x += 5
x -= 3
x *= 2
x /= 4
x %= 4
"""

# use case
salary = 10000
salary +=2000 #12000

steps = 1000
steps +=500   #1500

total = 0
item_price = 250
total += item_price

lives = 3
lives = -1

wallet = 1000
wallet -= 250
