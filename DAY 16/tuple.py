"""
Tuples Comprehension

Tuple Comprehension looks similar to list comprehension
1. Instead of producing list. It creates tuple like object called generator
2. Python does not support tuple comprehension
3. Python creates a generator not actual tuple

Example:
"""
t = ( x**2 for x in range(5))
print(t)

"""
If you really want a tuple, you must wrap the generator with tuple function.

Syntax:
tuple_variable = tuple(expression ;for item in iterable  ;condition)

1. Expression -> Operation or value to return
2. Item -> Variable representing each element from iterable
3. Iterable -> Sequence like list,range, string, tuple,etc.....
4. Condition (optional) -> Filter elements

Advantages:
1. Compact and readable code
2. Memory efficient when used as a generator
3. Easy transformation of sequences

"""
t = tuple(x**2 for x in range(5));print(t)


"""
Section 1 : Basic Tuple Comprehension

"""

t1 = tuple( x**2 for x in range(6)); print(t1)  #square of numbers
t2= tuple(x*2 for x in range(1,6));print(t2)  # print double 

words =['apple','banana','kiwi']   #length of words
t3 = tuple(len(ele)  for ele in words);print(t3)

t4 = tuple(ele  for ele in 'python');print(t4)   #convert string into tuple of characters
t5= tuple(i**3 for i in range(1,6));print(t5)  #cubes of numbers

t6 =tuple(ord(i) for i in 'abc');print(t6)  #ascii value of characters
t7 = tuple(w[0]   for w in ['sun','moon','star']);print(t7)  #first letter of each word
t8 = tuple(w[::-1] for w in ['cat','dog','owl']);print(t8) #reverse each word
t9= tuple(i  for i in range(10,16));print(t7)  #numbers from 10 to 15
# temperature conversion to F

temp =[0,20,37,100]
t10 = tuple((ele*9/5)+32  for ele in temp);print(t10)

"""
SECTION - 2
TUPLE COMPREHENSION - FILTERING ELEMENTS
WITH CONDITIONS

# Syntax
result = tuple(expression for item in iterable if condition)


"""
#1. even numbers till 10
t2_1 = tuple(ele   for ele in range(1,11)  if ele%2==0 );print(t2_1)

#2. Odd numbers
t2_2 = tuple( ele   for ele in range(1,50)  if ele%2==0);print(t2_2)

#3. Words start with a
words =['apple','banana','orange','avocardo','grapes','amla']
t2_3 = tuple(ele  for ele in words   if ele.startswith('a'));print(t2_3)

#4. Numbers greater than 50
nums = list(range(1,100,7))

t2_4 = tuple( ele   for ele in nums if ele>50 );print(t2_4)

# Multiples of 5
t2_5 = tuple( ele    for ele in range(1,51)  if ele%5==0);print(t2_5)

#6. Positive numbers

# 6. Positive numbers
nums = [-5, 3, 0, -1, 8]
t6 = tuple(x for x in nums if x > 0)

# 7. Names longer than 4 letters
names = ["Amy", "Jonathan", "Eva", "Michael"]
t7 = tuple(n for n in names if len(n) > 4)

# 8. Uppercase letters only
t8 = tuple(ch for ch in "PyThOn" if ch.isupper())

# 9. Numbers divisible by both 2 and 3
t9 = tuple(x for x in range(1,31) if x%2==0 and x%3==0)

# 10. Palindrome words
words = ["madam", "apple", "level", "world"]
t10 = tuple(w for w in words if w == w[::-1])

"""
Section 3 : Tuple Comprehension with Functions 
(Applying functions in comprehension)

"""
# 1. Square root of numbers
import math
t1 = tuple(math.sqrt(x) for x in range(1,6))

# 2. Factorial of numbers
t2 = tuple(math.factorial(x) for x in range(1,6))

# 3. Absolute values
nums = [-5, 3, -10, 0]
t3 = tuple(abs(x) for x in nums)

# 4. String lengths using len()
words = ["apple", "banana", "kiwi"]
t4 = tuple(len(w) for w in words)

# 5. Lowercase conversion
t5 = tuple(s.lower() for s in ["PYTHON", "JAVA", "C++"])

# 6. Uppercase conversion
t6 = tuple(s.upper() for s in ["python", "java", "c++"])

# 7. First letter capitalized
t7 = tuple(s.capitalize() for s in ["apple", "banana", "kiwi"])

# 8. Round float numbers
nums = [3.1416, 2.7182, 1.6180]
t8 = tuple(round(x, 2) for x in nums)

# 9. Strip spaces from words
t9 = tuple(s.strip() for s in ["  apple ", " banana ", " kiwi "])

# 10. Count vowels in each word
def count_vowels(word):
    return sum(1 for ch in word.lower() if ch in "aeiou")

words = ["apple", "banana", "kiwi"]
t10 = tuple(count_vowels(w) for w in words)

"""
#Section 4 : Nested Tuple Comprehension (Using two loops in comprehension)

"""

# 1. Multiplication table pairs
t1 = tuple((x, y, x*y) for x in range(1,4) for y in range(1,4))

# 2. Cartesian product of two lists
colors = ["red", "blue"]
fruits = ["apple", "banana"]
t2 = tuple((c, f) for c in colors for f in fruits)

# 3. Pairs of even numbers
t3 = tuple((x, y) for x in range(2,5) for y in range(6,9))

# 4. Sum of pairs
t4 = tuple(x+y for x in [1,2] for y in [3,4])

# 5. Concatenate strings
t5 = tuple(a+b for a in ["A", "B"] for b in ["X", "Y"])

# 6. All coordinate pairs in a 2x2 grid
t6 = tuple((x, y) for x in range(2) for y in range(2))

# 7. Multiplication results in one tuple
t7 = tuple(x*y for x in range(1,4) for y in range(1,4))

# 8. Flatten a nested list
nested = [[1, 2], [3, 4]]
t8 = tuple(num for sublist in nested for num in sublist)

# 9. Combinations of digits and letters
t9 = tuple(str(x)+y for x in range(1,3) for y in ["A", "B"])

# 10. Pairs where sum is even
t10 = tuple((x, y) for x in range(3) for y in range(3) if (x+y)%2==0)


