"""
Introduction to Sets Comprehension

A set comprehension is a concise way to create a Python 'set' in a single line,
using a syntax similar to list comprehensions but with curly braces {}.

Purpose:
--> Remove duplicates automatically (because sets store only unique elements.)
--> Write cleaner and shorter code
--> Apply transformations or filters in a single step.


Syntax:
{expression for item in iterable if condition}

Parts:
1. Expression : what value you want to include in set
2. Iterable : Sequence or collection to loop through
3. Condition : filters items



"""
#2. Basic set comprehensioons
# create a set by uterating over an iterable and applying an expression. Removes
# duplicates automatically.

#1. Square numbers from 1 to 5
squares ={x**2  for x in range(1,6)}
print(squares)


#2. Uppercase letters for a word
letters ={ch.upper() for ch in 'hello'};print(letters)


#3. First letter of given words
first_letters = { word[0] for word in ['apple','banana','cherry','apricot']}
print(first_letters)

#4. Even numbers from a list
evens ={x  for x in [1,2,3,2,4,4,6] if x%2==0};print(evens)


#5. Length of words
lengths = {len(word)   for word in ['cat','elephant','dog','ant']}
print(lengths)

#6. Absolute values
abs_values ={ abs(x) for x in [-1,-2,3,-4,3]};print(abs_values)


#7. Remove whitespaces from string
chars ={ ch  for ch in "hello world"  if ch!=" "};print(chars)

#8. Multiples of 3
multiples_3 = {x for x in range(1,20)  if x%3==0};print(multiples_3)

# Vowels in a sentence
vowels ={ ch for ch in "Python Programming" if ch.lower() in 'aeiou'}
print(vowels)

#10. REVERSE WORDS IN A LIST
reverse_words ={word[::-1] for word in ['apple','banana','pig','cat']}  
print(reverse_words)


"""
3. SET COMPREHENSION WITH CONDITIONS

"""

#1. ODD NUMBERS From 1 to 10
odds ={x for x in range(1,11) if x%2!=0};print(odds)

#2. Names starting with A
names_A ={name for name in['Alice','Bob','Andrew','Charlie'] if name.startswith('A')}
print(names_A)

#3. Numbers greater than 50
greater_50 ={ x for x in [12,55,78,30,99]  if x >50};print(greater_50)

#4. Words longer than 4 characters
l_words = { word for word in ['cat','dog','elephant','horse','donkey']  if len(word) > 4}
print(l_words)

#5. Positive numbers
p_numbers ={x  for x in [-2,3,-5,6,0,8]  if x >0};print(p_numbers)

#6. Consonants
consonants ={ ch for ch in "Hello World" if ch.lower() not in 'auiou'}
print(consonants)


#7. Numbers divisble for 2 and 3
div_2_3 ={i for i in range(1,30)  if i%2==0 and i%3==0};print(div_2_3)

#8. Non empty Strings
non_empty ={ word  for word in ["", 'apple','banana',"",'cherry'] if word}
print(non_empty)

#9. Prices greater than 100
expensives ={  price  for price in [50,100,120,300,80] if price > 100}
print(expensives)


#10. Only lowercases from string
lowercase_letters ={ ch for ch in "Python3.8" if ch.islower()}
print(lowercase_letters)

"""
4. Nested Set Comprehensions

You can use nested loops inside 

"""

#1. All products of two lists
products ={x*y for x in [1,2,3] for y in [4,5]};print(products)

#2. Pair of letters
pairs ={a+b for a in 'ab'  for b in '12'};print(pairs)

#3. Multiplication table (values only)
table ={i*j for i in range(1,4) for j in range(1,4)}
print(table)

#4. Sum of two ranges
sum_pairs ={x+y for x in range(3)  for y in range(3)}
print(sum_pairs)

# Unique character pairs from strings
char_pairs ={ a+b for a in 'hi' for b in 'ok'};print(char_pairs)

#6. All coordinates in a 2*2 grid
coordinates ={(x,y)  for x in range(2)  for y in range(2)};print(coordinates)

#7. Concatenate names and titles
full_names ={title + name  for title in ['Mr','Ms']  for name in ['John','Emma']}
print(full_names)

#8.Common multiples of 2 and 5
common_mult ={x*y  for x in [2,4] for y in [5,10]};print(common_mult)

# 9: Word pairs from two lists
word_pairs = {w1 + " " + w2 for w1 in ["red", "blue"] for w2 in ["car", "bike"]}
print(word_pairs)

# 10: Cross product of sets
cross_product = {m+n for m in {"A", "B"} for n in {"1", "2"}}
print(cross_product)