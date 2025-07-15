# STRINGS

#Defining a string

""" 
A string is a sequence of characters assigned in a singlw quotes '.......'
or double quotes "......."
Both single and doubke quotes can be used to define a  string.
However, it's generally recommended to use a single quotes for strings
that contain double quotes and vice versa.

"""

#Examples:
string1= 'Hello World' #single quotes
string2 = "Hello World" #double quotes
print(string1) #Hello World
print(string2) #Hello World

#Accessing elements of the string
""" 
You can access characters using indexing and slicing.
Strings are sequences, so you can access their elements using indexing.
Indexing starts at 0, so the first character is at index 0.

"""

#Example:
#Indexing at zero 

word = "Python"
print(word[0]) #output :P
print(word[2]) #output :t

#Negative indexing : -1 from the end
print(word[-1]) #output -n
print(word[-3]) #output : h

#Slicing (returns a substtring)
print(word[1:4])  #output :yth (characters at index 1,2,3)
#print(word[1:])   #output :ython (characters at index 1 to the end)
print(word[:3]) #output:Pyt (from start (0) till 2)
print(word[3:]) #output :hon ( from index 3 till the end)


#String Methods:
""" 
Strings have several methods that can be used to perform various operations.
Some of the most commonly used methods are listed below:
- len() : returns the length of the string
- lower() : returns the string in lowercase version.
- upper() : returns the string in uppercase version
- title() : returns the string with the first character of each word capitalized
- replace() : replaces a substring with another substring
- split() : splits a string into a list of substrings
- join() : joins a list of strings into a single string
- strip() : removes leading and trailing whitespace


- find() : returns the index of the first occurrence of a substring
- rfind() : returns the index of the last occurrence of a substring
- lstrip() : removes leading whitespace
- rstrip() : removes trailing whitespace
- capitalize() : returns the string with the first character capitalized
- count() : returns the number of occurrences of a substring
- center() : returns a string centered within a specified width
- ljust() : returns a string left-justified within a specified width
- rjust() : returns a string right-justified within a specified width
- zfill() : pads a numeric string with zeros on the left
- isalnum() : returns True if all characters in the string are alphanumeric
- isalpha() : returns True if all characters in the string are alphabets
- isdigit() : returns True if all characters in the string are digits
- islower() : returns True if all cased characters in the string are lowercase
- isupper() : returns True if all cased characters in the string are uppercase
- isspace() : returns True if all characters in the string are whitespace

- startswith() : returns True if the string starts with a specified value
- endswith() : returns True if the string ends with a specified value
- isalnum() : returns True if all characters in the string are alphanumeric
- isdigit() : returns True if all characters in the string are digits
- islower() : returns True if all characters in the string are lowercase
- isupper() : returns True if all characters in the string are uppercase


"""

text='Hello World'
print(text.upper())
print(text.lower())
print(len(text))
print(text.title())
print(text.strip()) 
print(text.replace('World','Python'))
print(text.split()) #returns a list of words
print(' '.join(text.split())) #returns a string of words with spaces in between
print(text.find('World'))
print(text.rfind('World'))
print(text.lstrip()) #removes trailing white spaces

print(text.find("World"))
print(text.rfind("World"))
print(text.count("World"))
print(text.startswith("H"))
print(text.endswith("d"))
print(text.isalnum())
print(text.center(20))
print(text.ljust(20))
print(text.rjust(20))


#Type-casting
""" 
Type casting is the process of converting a value from one datatype to another
Foe example:
- int() : converts a value to integer
- float() : converts a value to float
- str() : converts a value to string
- bool() : converts a value to boolean
- complex() : converts a value to complex number
"""

num =100;text = str(num)
print(text,type(text)) #ouput: <class 'str'>

#Converting string to an integer
print(int('12345'))

#Converting string to float
print(float('234.546'))   #output :234.546

# Converting string to boolean
print(bool("True")) #output : True
print(bool("False")) # output : False

print("""
🧠 Python bool() Conversion Notes (String Edition)

1️⃣ General Rule:
- bool(x) returns False only if x is:
    - None
    - False
    - 0, 0.0
    - '' (empty string)
    - [], {}, () (empty containers)
- Everything else (non-empty, non-zero) → True

2️⃣ For Strings:
- bool("")        → False      # Empty string
- bool("False")   → True       # Non-empty string
- bool("0")       → True       # Still a string, not number
- bool(" ")       → True       # A space is a character

📌 Important:
- Python does NOT check the *content* of the string.
- It only checks if it's empty or not.
- So, even if a string says "False", it's still a non-empty string → True

❗ Common Confusion:
- bool("False")         → True
- "False" == False      → False  (string ≠ boolean)
- bool("False") == True → True

3️⃣ Convert string to actual boolean (based on text content):
Use:
    s = "False"
    b = s.lower() == "true"   → False

4️⃣ Safe Custom Function:
    def str_to_bool(s):
        return str(s).strip().lower() == "true"

    print(str_to_bool("True"))     → True
    print(str_to_bool("FALSE"))    → False
    print(str_to_bool(""))         → False
    print(str_to_bool(" true "))   → True  (handles spaces and case)

✅ Summary:
- bool("False") is True because the string is non-empty.
- Use content checking if you want "True"/"False" as actual boolean logic.
""")

print(bool(0)) #output : False
print(bool(1)) #output : True
print(bool(0.0)) #output : False
print(bool(1.0)) #output : True
print(bool(None)) #output : False


#Convert string to a list
print(list("123"))  #output :['1','2','3']
print(list("12345"))  #output :['1','2','3','4','5']

# Converting string to tuple
print(tuple('100498')) #ouput : ('1','0','0','4','9','8')

#Converting string to dictionary
# print(dict('123')) #output :{'1':None,'2':None,'3':Non

#Converting string to set
print(set('123')) #output :{'1','2','3'}

# Converting a string to a complex
print(complex("123.45"))   #output : 123.45+0j


#Converting string to frozenset
print(frozenset('123')) #output :frozenset({'1','2','3'}}

# Input Output

"""
You can get input from the user using input() and 
print output using print()
"""

# String Formatting
""" 
You can format a string to include variables dynamically
"""

#✅ Using f-strings ( Python 3.6+)
name= "Alice";age=25; print(f"Hello my name is {name} and I am{age} years old ")
pet="peelu";print(f"My pet love bird name is {pet}")

#✅ Using the % operator
#The % operator is a simple way to format strings in Python.

name="Bob";age =30
print("My name is %s and I am %d years old"% (name,age))

#✅ Using the format method

print("My name is {}".format(name))

#✅ Using the string concatenation
# String concatenation is a way to combine two or more strings 
# into a single string.

name="Charlie";age=35
print("My name is "+name+" and I am "+str(age)+" years old")
