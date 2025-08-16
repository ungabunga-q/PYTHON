"""
Dictionary Comprehension

A concise way to creare dictionary in a single line using
{key,value  for ...............} syntax

General Syntax:
{key_expr : value_expr for itwm in iterable if condition}


Advantages:
# 1. Short and readable
# 2. Often faster than loops
# 3. Easy to apply condition

"""

#2. Basic Dictionary Comprehension
# Convert iterable data into dictionary

#1. Square of numbers 1-5
a = {n:n**2  for n in range(1,6)};print(a)

#2. Map words to their lengths
w_length = { word:len(word)  for word in ['apple','banana','cherry']}
print(w_length)

#3. Index to letter mapping
i_l_mapping ={ i:chr(65+i)   for i in range(5)}
print(i_l_mapping)


#4. Even numbers and their cubes
even_n_cube ={i:i**3  for i in range(2,37,2) }
print(even_n_cube)

#5. Character Frequency
ch_freq ={ch:'vowel'  for ch in 'aeiou'};print(ch_freq)

#6. Mapping number to its Square root
s_r ={ n:round(n**0.5,2)   for n in range(1,6)};print(s_r)

#7. Convert list of tuples into dict
dict_tup ={k:v  for k,v in [('a',1),('b',2)]};print(dict_tup)

#8. Reverse key value in dictionary
rev_dict ={ v:k  for k,v in [('a',1),('b',2)]};print(rev_dict)

#9. Number to binary mapping
bin_rev ={i:bin(i)   for i in range(1,6)};print(bin_rev)

#10. Zip two lists into dict
zip_dict ={k:v for k,v in zip(['name','age'],['Alice',25])}
print(zip_dict)

"""

Section 3:
Conditional Dictionary Comprehension

"""
#1. Even numbers only
even_dict ={ i:i**2  for i in range(10)  if i%2==0};print(even_dict)

#2. Words longer than 4
w_len_4 ={ele:len(ele)  for ele in ['pen','pencil','marker'] if len(ele)>4}
print(w_len_4)

#3. Positive numbers only
pos_dict ={x:x**2 for x in [-2,-1,0,1,2,3,4] if x >0 };print(pos_dict)

#4. Vowels only from string

v_s ={c:ord(c)   for c in 'education' if c in 'aeiou'}
print(v_s)



