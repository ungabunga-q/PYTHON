"""
DAY 16
DATE -14TH AUGUST 2025

A List comprehension is a concise way to create lists in Python 
using a single line of code

Syntax: 
[ expression  for an item in iterable   if condition]

Benefits :

1. Shorter and cleanest code
2. Faster than using loops [ in most cases]
3. More Pythonic ( recommended style)

"""

# Section 1 : Basic List Comprehension [ No condition]
# Directly apply an operation or transformation on each element of an iterable

# Syntax : 
# [Expression  for an item in iterable ]

#1. Square numbers from 1 to 9
squares = [i**2   for i in range(1,10)];print(squares)

#2. Convert strings to uppercase
words =['python','java','c++']
upper_words = [ele.upper()  for ele in words];print(upper_words)

#3. Get length of each word
len_word =[len(ele)   for ele in words];print(len_word)

#4. Multiplu each by 10
nums =[1,2,3]
times_10 = [ele*10  for ele in nums]
print(times_10)


#5. Convert list of numbers to string
num_str = [str(i)  for i in [10,20,30]]
print(num_str)


#6. Add 5 to each number
plus_5 =[i+5  for i in range(1,6)];print(plus_5)

#7. Cube of each number
cubes =[n**3   for n in range(1,6)];print(cubes)

#8. Double characters in a string
doubled =[ch*2   for ch in 'hello'];print(doubled)

#9. First letter of each name
names =['Alice','Bob','Charlie']
f_letters = [ele[0]  for ele in names];print(f_letters)

#10. Reverse each word
reversed_words = [ele[::-1]  for ele in ['apple','banana','cherry']]
print(reversed_words)

"""
Section 2 : List Comprehension with condition

# Filter elements while building the list

# Syntax: 
# [ expression  for item in iterable if condition]


"""
#1. Even numbers from 1 to 20
evens = [ele  for ele in range(1,21) if ele%2==0 ];print(evens)

#2. Odd numbers from 1 to 20
odd = [ele  for ele in range(1,21) if ele%2!=0 ];print(odd)

#3. Numbers greater than 5
n_5 = [ i  for i in range(1,10)  if i>5 ];print(n_5)


#4. Words starting with p
words =['python','perl','C++','java']
starts_with_p = [ele  for ele in words  if ele.startswith('p') ];print(starts_with_p)

#5. Words longer than 4 letters
long_words = [ele   for ele in words  if len(ele) >4] ;print(long_words)


#6. Positive numbers only
nums =[-3,-2,-1,0,1,2,3]
pos_nums =[n   for n in nums if n >0] ;print(pos_nums)

#7. String containing 'a'
contains_a = [w  for w in ['cat','dog','apple']  if 'a' in w];print(contains_a)

#8. Numbers divisble by both 2 and 3
divisible =[ x for x in range(1,30) if x%2==0 and x%3==0]
print(divisible)

#9. Skip empty Strings
names =['John',"","Sam",""]
non_empty = [ele for ele in names if ele];print(non_empty)

#10. Words not equal to Java
print(words)
not_java =[w for w in words if w!='java'];print(not_java)

"""
Section 3 : List Comprehennsion with if-else condition
Apply a transformation depending on a condition

Syntax:
[  true  if condition else false  for item in iterable]

"""

#1. Label numbers as even or odd
labels =['even ' if n%2==0  else 'odd' for n in range(10)]
print(labels)

#2. Replace negatives with 0
nums =[ -5,3,-1,7]
no_negatives =[ ele  if ele >0 else 0 for ele in nums ]
print(no_negatives)


#3. Pass/ Fail based on marks
marks =[45,8,30,95]
result =  [ "Pass" if ele >=40 else "Fail"  for ele in marks]
print(result)

#4. Convert numbers to strings if n > 10
nums=[5,12,7]
converted =[str(ele) if ele >10 else ele  for ele in nums]
print(converted)


#5. Grade students
scores =[90,70,40,20]
grades =['A'  if ele>=80  else 'B' if ele>=50 else 'C' for ele in scores]
print(grades)


#6. Replace even numbers with double, odd numbers unchanged
nums =[1,2,3,4]
modified =[n*2 if n%2==0 else n  for n in nums];print(modified)

#7. Uppercase Short words ,lowercase long words
words =['hi','HELLO','bye','GoodMorning']
case_change =[ele.upper() if len(ele) <=3 else ele.lower()    for ele in words]
print(case_change)

#8. Tag positive/negative numbers
num =[-3,-1,0,2,4]
tagged =["Positive" if item>0 else 'Negative'  for item in num];print(tagged)
# add condition for zero 

#9. Replace vowels with *
chars =['a','b','c','e','f']
vowels_replace = ["*" if ch in 'aeiou' else ch  for ch in chars]
print(vowels_replace)

#10. Append suffix '_ok' if string length <5
words =['cat','python','dog']
append_w = [ ele+'_ok' if len(ele) <5  else ele for ele in words]
print(append_w)

"""
Section 4
Nested List Comprehension

# Used for two or more loops

"""

#1. Cartesian Product of two lists
product =[(x,y)   for x in [1,2,3]  for y in ['a','b']];print(product)

#2. Flatten a 2d List
matrix =[[1,2,3],[4,5],[6,7]]
flat =[ j   for row in matrix for j in row];print(flat)

#3. All pairs (i,j)  where i<j
pairs =[(i,j)  for i in range(3)  for j in range(3)  if i<j]
print(pairs)

#4. Multiplication table (1,3)
table =[f"{i}*{j}={i*j}"  for i in range(1,4)  for j in range(1,11)]
print(table)
for ele in table:
    print(ele)

#5. Combine adjectives with nouns
adjectives =['red','big']
nouns =['apple','car']
combinations =[ ele+" "+ele1  for ele in adjectives for ele1 in nouns]
print(combinations)


#6. All possible coordinates 
coords =[ (x,y,z)   for x in range(2)  for y in range(2) for z in range (2)]
print(coords)


#7. Extract diagonal elements from matrix
matrix =[[1,2,3],[4,5,6],[7,8,9]]
dig =[matrix[i][i]     for i in range(len(matrix))]
print(dig)


#8. Reverse each word in sentences
sentences =[['hello','world'],['python','rocks']]
reversed_sen =[ ele[::-1]    for ele in sentences  for w in ele]
print(reversed_sen)

#9. Get even numbers from multiple lists
lists =[[1,2,3],[4,5,6],[7,8,9]]
evens =[ n     for item in lists  for n in item if n%2==0]
print(evens)

#10. Combine letters from two words
letters =[a+b  for a in 'ab'  for b in '12']
print(letters)

"""
Section 5:

Using functions inside list comprehension

"""

#1. Square using pow()
squares =[ pow(n,2)  for n in range(5)]
print(squares)

#2. Strip spaces from strings
words =['   apple','banana   ','cherry   ']
cleaned =[ w.strip()  for w in words];print(cleaned)

#3. Get absolute values
nums =[-5,-1,0,3]
abs_values =[ abs(n) for n in nums];print(abs_values)

#4. Convert to title case
names =[ 'john doe','jane smith']
titles =[ele.title()   for ele in names];print(titles)

#5. Length of each sentence
sentence =['Hello World','Python is fun']
len_sen =[ len(ele)  for ele in sentence];print(len_sen)

#6. Find factorial of numbers
import math
fact = [ math.factorial(n)  for n in range(6)]
print(fact)


#7. Convert float to int
floats =[2.5,3.7,8.1]
ints =[int(ele) for ele in floats]
print(ints)

#8. Count vowels in words
count_vowels = [sum( 1 for ch in w if ch in 'aeiou')  for w in ['apple','banana']]
print(count_vowels)


#9. Check pallindrome
p_c =[w==w[::-1]  for w in ['madam','cat','racecar']]
print(p_c)

#10. Round off numbers
rounded =[round(n,1)   for n in [1.234,5.678,9.876]];print(rounded)
