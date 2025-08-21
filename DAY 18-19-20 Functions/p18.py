"""
Introduction to Functions:

--> What is a function?

A function is a block of reuseable code that performs a specific task.

Instead of writing the same code again and again, we can write it
once inside a function and call it whenevr needed.


--> Importance of functions in programming.

A. Breaks large programs into smaller parts.
B. Increases readability and maintainability.
C. Encourages code reuse.


--> Advantages:
a. Code Reuseability - write once, use many times
b. Readability - Clean and understandable cpde
c. Modularity - Breals programs into smaller logical parts
d. Easy Debugging - Errors can easily be identified into specific functions.



--> Function naming rules
a. Must start with a letter or underscore
b. Cannot start with a digit
c. Can contain letters ,digit, underscores
d. Avoid Python keywords [ def , for, while , etc...]


--> Indentation Importance:
a. Python uses identation to define block of code
b. Wrong indentation -> Indentation Error


3. Types of Functions
In Python, functions are divided into two major categories
1. Built- In functions
2. User defined functions

--> Built - in Functions [ eg- print(),len(),type()]

These functions are already defined in Python.
We don't need to create them; just use them directly.
They make development faster and easier
Python provides hundreds of built-in function.

************************************************************
Examples of commonly used built-in functions
************************************************************

a. print()- Displays output
b. len() - Returns length of a sequence
c. type() - Returns the datatype of a variable
d. max()/min() - Find maximum/minimum value
e. sorted() - Returns sorted list
f. sum() - Contains the sum of elements.
g. abs() - Returns the absolute value
h. round() - Round a floating number
i. input() - Takes input from user
j. zip() -Combines multiple iterables
"""

#Types of built-in functions
"""
1. Numeric Functions:
These work with numbers [ integers, float , complex].
They help in mathematical operations.

a. abs(x) -> Returns absolute value
b. round(x,n) -> Rounds number to n decimal places
c. pow(x,y) ->Returns x^y
d. min(),maz() -> Minimum /Maximum
e. sum(iterable) -> Sum of numbers

"""

#1. abs() with positive and negative numbers
print(abs(-25))
print(abs(15))

#2. round with floating numbers
print(round(3.14159,2))
print(round(9.876,1))

#3. pow() to calculate powers
print(pow(2,3))
print(pow(5,2))

#4.max() to find largest
print(max(10,20,5,99))

#5.min() to find smallest
print(min([44,11,67,3]))

#6. sum() with list
nums = [i  for i in range(10,41,10)]
print(f" Sum : {sum(nums)}")

#7. Round without decimal
print(round(45.678))

#8. abs()  with complex number magnitude
print(abs(3+5j))

#9. Pow() with negative number
print(pow(2,-2)) #1/2^2

#10. Calculating min,max,sum
marks =[75,88,92,60,85]
print(f"Higest marks {max(marks)}")
print(f"Lowest marks : {min(marks)}")
print(f"Sum of marks : {sum(marks)}")


"""
Type Conversion Functions:
These convert one datatype to another

a.int(x)  -> Convert to integer
b.float(x) -> Convert to float
c. str(x)  -> Convert to string
d. list(x) -> Convert to list
e. tuple(x) ->Convert to tuple
f. set(x)  -> Convert to set

"""

#1. int() from float
print(int(9.99))

#2. int() from string
print(int('123'))

print(float(10))  #float from int
print(float('45.67'))  #float from string

#5. str() from num
num = 99 ; print(f"Converted to string : {str(num)}")

#6. List() from tuple
tup =(1,2,3);print(list(tup))

#7. Tuple from list
lst =[10,20,30];print(tuple(lst))

#8.  set()  from list [ removes duplicate]
lst2 =[1,2,3,4,4,5,64,53,3,2,3]
print(set(lst2))

#9. str() from boolean
print(str(True))

#10. Nested converstions
print(list("Python"))


"""
3. String-related Functions
These work on strings and characters

1.len(string)  -> Returns Length
2.ord(ch) -> ADCII CODE OF CHARACTER
3.ch(num)   -> Character of ascii code
4. str.upper(),str.lower()  -> Convert case
5.str.split() -> Splits into lists
6. str.join()  -> Join list into string
"""

#1.len() with string
print(len('Programming'))

#2. ord()  with character
print(ord('A'))

#3. chr() with ASCII NUMBER
print(chr(66))

#4. upper()
print('Python'.upper())

#5. Lower ()
print('Hello'.lower())

#6. Split()
sentence ='I love Python Programming'
print(sentence.split())

#7. Join( ) to join list with spaces
words =['I','Love','python'];print(" ".join(words))

#8. Join() with comma
print(",".join(words))

#9. Combine len+upper
s='functions';print(len(s.upper()))

#10. mix ord+chr
code =ord('Z')
print(f"Code : {code} -> Character: {chr(code)}")

"""
Iterables and Collection Functions:
a. Sorted() -> Returns sorted list
b. enumerate(iterable) -> Gives index and element
c. zip(iter1,iter2)  -> Combines sequences
d.map (func,iterable) -> applies function
e. filter(func,iterable) -> Filters elements

"""

#1. sorted() on list
nums =[5,2,9,1,7];print(sorted(nums))

#2. sorted() on string
print(sorted("Python"))

#3. Enumerate with list
fruits =['apple','banana','mango']
for i,fruit in enumerate(fruits,start=1):
    print(i,fruit)
    
    
#4. zip two lists
names =['Amit','Neha','Raj'];marks=[90,85,88]
print(list(zip(names,marks)))
#print(zip(names,marks))


# 5. Zip with 3 lists
subjects =['Math','Science','English']
print(list(zip(names,marks,subjects)))

#6. Map with lambda to square numbers
num1 =[1,2,3,4]
sq_lambda =list(map(lambda x:x**2,nums))
print(sq_lambda)

#7. Filter to find even numbers
evens = list(filter(lambda x:x%2==0,range(1,11)));print(evens)

#8. Map with str upper
names23 =['Python','java','c++']
print(list(map(str.upper,names23)))

#9. Filter to find name starting with A
names2=['Amit','Ravi','Anita','Kiran']
print(list(filter(lambda x:x.startswith('A'),names2)))

#10. Combine map + filter
nums =[1,2,3,4,5,6]
result =list(map(lambda x:x**2,filter(lambda y:y%2==0,nums)))
print(result)


"""
5. Input/Output Functions
a.print() ->Display output
b. input() -> Take input

"""

#1. Basic Print
print("Hello, Python!")

#2. Print multiples values
print('Sum of 5 and 10',5+10)

#3. Print with separator
print("Python",'Java','C++',sep=" | ")

#4. Print with end parameter
print("Hello",end=" ")
print("World")

#5. Input integer
int_age =int(input("Enter your age :"))
print(f"You are {int_age} years old")

#6.Input name
int_name = input("Enter name :")
print(f"Your name is {int_name}")

#7. Input float
price = float(input("Enter price : "))
print(f"Final Price is {price}")

#8. Using input() in calculations
a =int(input("Enter first number :"))
b=int(input("Enter second number:"))
print(f"Sum is {a+b}")

#9. Formatted String
print(f"Name :{int_name}, age : {int_age}")

#10. Print with format
print('The pricr is {:.2f}'.format(price))