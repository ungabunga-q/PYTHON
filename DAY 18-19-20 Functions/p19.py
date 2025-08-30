# User Defined Functions

"""
--> User Defined Functions [Custom Created by Programmers]

a. Functions that are created by the programmer using the def key word.
b. Useful when we want to perform a task repeatedly with our own logic.

Structures definition -> calling execution

--> Steps to use User-Defined functions:

a.  Define the function using def.
b. Call the function by its own name.
c. (Optional ) Pass parameters and use return if needed


--> Structure of a user-defined function:

"""

def function(parameters):
    """ docstring [optional]"""
    #body of a function
    value=1
    return value #optional


#1. Simple function without parameter
def great():
    """ simple func"""
    print('Hello, Welcome to Python Functions!')

great()

#2. Function with parameter
def welcome(name):
    print(f"Hello {name}")

welcome('Aishwarya')

#3. Function with multiple parameters
def add(a,b):
    print(F"Sum {a+b}")
    
add(10,5)

#4. Function with returb statement
def cube(num):
    return num**3
print(f"Cube of 4: {cube(4)}")

#5. Function returning multiple values

def math_operations(a,b):
    return a+b,a-b,a*b,a/b

print('Results',math_operations(20,5))

#6. Function with default parameter
def info(city='Mumabi'):
    print('I live in ',city)

info()
info('Delhi')

#7. Function to check even/odd
def chk_even(num):
    if num%2==0:
        print(f'Even')
    else:
        print(f'Odd')
chk_even(5)


#8. Function to reverse a string
def reverse_string(s):
    return s[::-1]

print(f"Reverse: ",reverse_string('Python'))


#9. Functions with loop [Factorial]

def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact *=i
    return fact

print(f"Factorial of {5} is {factorial(5)}")

#10. Nested Functions [ function inside function ]

def outer():
    def inner():
        print("This is inner function")
    print("This is outer function")
    inner()
outer()

"""

5. Function Call and Return Statement

- To use a function, we call it using its name followed by parentheses.
- The return keyword sends a value back to the caller.

A function can:
- Return nothing[ Default-> None]
- Returns a single value
- Returns multiple values

Difference between print() and return
- print() -> Displays output on screen
- return() -> Sends value back to program for further use


"""
#1. Function call
def hello():
    print('Hello World!')

hello()

#2. Function with return
def square(n):
    return n**2
print(f"Square of 5:",square(5))

#3. Function with multiple returns 
def calc(a,b):
    return a+b
res = calc(10,3)
print(f'Results ',res)

#4. Function with return vs print

def show1():
    print('Inside show1')
def show2():
    return 'Inside show2'

show1()
print(show2())


#5. Return used in calculation
def double(x):
    return x*2
print(f"Double of 8:",double(8))

#6. Return None explicitly
def test():
    return None
print(test())


#7. Early Return
def divide(a,b):
    if b==0:
        return 'Division by Zero not allowed'
    return a+b
print(divide(10,0))
print(divide(10,2))

#8. Function inside another function call
def increment(x):
    return x +1

print(f"Result: ",increment(square(4)))


#9. Returning string
def greet(name):
    return f"Hello, {name}"

print(greet('Python'))

# function with multiple values unpacked
def stats(lst):
    return max(lst),min(lst),sum(lst)
high, low, total = stats([10,20,30,40])
print(f"High: {high} Low: {low} Sum:{total}")


"""
6. Functions with and without parameters

There are 4 categories:

- Without parameters and without return
- With parameters and without return
- Without parameters and with return
- With parameters and with return

"""

#1. without parameters and without return
def greet():
    print("Good, Morning!")
    
greet()

#2. With parameters and without return
def welcome(name):
    print(f'Hello, {name}')
welcome('Aishwarya')


#3. Without parameters and with return
def get_pi():
    return 3.14159
print(get_pi())

#4. With parameters and with return
def add(a,b):
    return a+b
print(f"Sum: {add(5,7)}")

#5. Function with default parameter
def message(msg='Hii'):
    return msg
print(message())
print(message("Hello World!"))

#6. Function with multiple return values
def operations(a,b):
    return a+b,a-b,a*b
print(operations(8,2))

#7. Function returning list
def square(n):
    return [i*i for i in range(1,(n+1))]
print(square(5))

#8. Function with string input
def reverse(s):
    return s[::-1]
print(reverse('Python'))

#9. Function with no arguement  but user input

def user_input():
    n = int(input("Enter Number: "))
    return n**2

print(f"Double : ",user_input())

#10. Functions with multiple arguements
def average(*args):
    return sum(args)/len(args)

print("Average :",average(10,20,30,40))

"""
7. Local and Global Variables"""


