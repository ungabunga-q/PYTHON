"""
1. What is Python Programming?

Python is a high-level, interpreted, general purpose programming language.
It was designed to be easy to read and write, making it ideal for beginners and
professionals alike.
Python is popular in web development, data science, automation, AI/ML, game development,
and much more.

Real life Examples:
1. Instagram and Youtube use Python for backend.
2. Google uses Python for many of its internal tools and APIs.
3. NASA uses Python for many of its scientific computing tasks.
4.Python scripts are used to automate Excel
5. You can create chatbots, calculators, games and apps

"""

# 1. Using print() Function
print("Hello World!")
print("Python is a great language!")

#2. Print with Multiple Arguements
name= 'Aishwarya'
age = 27
print("Name: ",name,"Age: ",age)



#3. Using sTRING CONCATENATION
first ="Hello"
second = 'World'
print(first + " " + second)


"""
2. History of Python
Python was first released in 1991 by Guido van Rossum.
It was created as a scripting language, but it has since grown into a full-fledged programming language.
Python 2.0 was released in 2000, and it introduced many new features, including
a garbage collector, Unicode support, and a more modern syntax.
Python 3.0 was released in 2008, and it introduced many changes, including 
a new syntax for division, a new way to handle exceptions, and a new way to handle strings.


It was named after the British comedy group "Monty Python"
Python's philosophy emphasises code readability, using indentation rather than curly braces.

Versions : Python 2 (LEGACY)
Python 3 (CURRENT)

"""

"""
3. Why Learn Python?

Benefits:
1. Simple and easy to learn
2. High demand in the job market
3. Can be used for web development, data analysis, machine learning, automation, and more
4. Cross-platform (can run on Windows, macOS, and Linux)
5. Vast libraries and community support
4. Great for both small scripts and large applications.

"""
"""
Use Cases:
1. Web Development ( Django, Flask)
2. Data Analysis ( Pandas, Numpy)
3. Machine Learning (scikit-learn, tensorflow)


4. Variable
A variable is a name that stores a value. In Python, you don't need to declare the type.

Rules:
1. Must start with a letter or underscore ( ex-name,_name)
2. Can't stand with a number example 25true
3. Can't contain special characters,space  except underscore (ex- name!name)
4. Can include letters, digits, underscores

"""

name = "Aishwarya"
age = 27
height = 154.5

print("Name: ",name)
print("Age: ",age)
print("Height: ",height)


"""
5. Keywords

Keywords are reserved words that have a special meaning in Python.
They cannot be used as variable names.

Examples:
False, True, None , if , else, elif, while
for, break, continue, def, return , import
as, class, try, except.

"""
# Using some keyword in a program
is_Married = True
print(is_Married)

"""
6. Comments and Statements
Statements -->
Instructions that Python can execute

Comments -->
Lines of code that Python ignores
Used to example the code

Single-line Comment: Starts with #
Multi-line Comment: Starts with " " " or ''' 

"""

# This is a single line comment
name = "Aishwarya" #storing name
print(name)

"""
7. Python Character SET
Character set refers to all the valid characters Python understands including:
1.Letters - A TO Z, a to Z
2.Digits - 0 TO 9
3.Special Characters - !, @, #, $, %, ^, &, *, (, ),
4. Whitespace- space,tab,newline
5. Escape Sequence - \n, \t, \r, \b, \f,
6. Special Symbols- + - * / = () {} [] etc.
7. Other charactes - Unicode characters

"""

# to execute a selected part in Python file  -->select code --> Shift + Enter


# using lettes, digits, special characters
a=10
b=20
sum = a+b
print("Sum: ",sum)

# Using whitespace for indentation
if a <b:
    print(a," is smaller than ",b)
else:
    print(a," is greater than ",b) #whitespace used before print


# -------------------------------------------------------------
#Example 1 : Simple input
print("Give input: ")
a= input()
print("You entered: ",a)


# Example 2 : Enter your name
name = input("Enter your name: ")
print("Hello ",name)

# Example 3: Input two numbers and add them
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

sum = int(num1) + int(num2) #convert to integers
print(sum)

# Example 4: Input and multiply two decimal numbers
x= float(input("Enter first number:"))
y= float(input("Enter second number:"))
print("Product =",x*y) # multiply two decimal numbers   

# Example 5: Input and calculate average of three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
print("Average =",(num1+num2+num3)/3) # calculate average of


#Example 6: Input age and print eligibility
age = int(input("Enter your age: "))
if age >=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#Example 5: Calculate Area of a Rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = length * width
print("Area of rectangle is: ",area)
