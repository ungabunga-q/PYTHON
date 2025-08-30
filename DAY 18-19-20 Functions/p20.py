"""
7. Local and Global Variables

- Local variable: Declared inside a function -> Accessible only inside it
- Global variable : Declared outside functions -> Accessible everywhere
global keyword allows modifications of a global variables inside a function

"""

#1. Global variable
x = 10
def show():
    print("x = ",x)
    
show()

# 2. Local variable
def local_demo():
    y = 5
    print(f" Local y = {y}")
local_demo()

# 3. Same name global and local
x = 100
def test():
    x = 50
    print(f" Local x = {x}")
test()

# 4. Access global inside function
count = 0
def increment():
    global count 
    count +=1
print("Before : ",count)
increment()
print("After :",count)

# 5. Functions modifying global
g='Python'
def change():
    global g
    g ='Java'
change()
print("Now g:",g)

# 6. Local variable shadowing
a = 10
def shadow():
    a =20
    print(f" Inside of ",a)
shadow()
print(f" Outside of ",a)


# 7. Return local variable
def calc():
    num = 42
    return num
print(calc())


# 8. Using the global inside loop
total = 0
def add_items(lst):
    global total
    for i in lst:
        total +=i
add_items([1,2,3])
print("Total =",total)


# 9. Function with both global and local
m = 5
def func():
    n =10
    print("Global ",m," Local  ",n)
    
func()

#10. No Global Modification
x= 10
def no_change():
    print("Inside: ",x)
no_change()
print("Outside : ",x)

"""
8. Lambda [Anonymous Functions]

- A lambda function in Python is a small, anonymous function [ A function
without a name.]
- It is mainly used for short, simple operations where defining a  full function
with def would be unnecessary.

Syntax: Lambda arguements : expressions

- lambda -> keyword to define
- arguements -> inputs to the function
- expressions -> single statement that returns the value

"""

# Example:
square = lambda x:x**2
print(square(5))

"""
Useage of Lambda with Functions

- map() - Applies a function to each element of a sequence
- filter() - Filters elements based on a condition
- reduce() - Reduce a sequence to a single value [ requires functools]

"""

# 1. Lambda to add two numbers
add = lambda a,b:a+b
print(add(2,3))

#2. square

square = lambda x:x**2
print(square(7))


# 3. Lambda with map to double list
# map - applies to each element
nums = [1,2,3,4,5]
doubled = list(map(lambda x:x*2,nums))
print(doubled)

#4. Lambda with map convert list of strings to uppercase
words =['apple','banana','cherry']
upper_words =list(map(lambda w: w.upper(),words));print(upper_words)

#5. Filter to get evens
evens = list(filter( lambda x:x%2==0,nums));print(evens)

# 6. Lamda with filter to get words starting with a
a_words = list(filter(lambda w: w.startswith('a'),words));print(a_words)

# 7. Lambda with reduce( ) to find calculate
from functools import reduce
total = reduce(lambda x,y:x+y,nums );print(total)

#8. Lambda with reduce to find maximum
maximum = reduce(lambda a,b: a if a>b else b,nums)
print(maximum)