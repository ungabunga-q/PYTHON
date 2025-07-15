""" 
STRING FORMATTING
"""

# 1. USING F- STRING
name ="Alice"; print(f"Hello ,{name}")

#2. multiple variables with format()
age =30;city ="Paris"
print("I am {} and I live in {}".format(age,city))

#3. Using % operator with strings
language ="Python";print("I have %s programming!" % language)

#4. Formatting with two decimal places
price =19.99 ; print(f"Price : ${price:.2f}") # doubt 

#5. Zero padding number
order =7;print(f"Order number is {order:03}")

#6. Allign text to right
text = "Welcome"; 
print(f"{text}")
print(f"{text:>20}")

#7. Align text to left
print(f"{text:<20}end")

#8. CENTER TEXT
print(F"{text:^20}")

#9. ESCAPING CURLY BRACES
print(F"{{THIS IS INSIDE CURLY BRACES}}")

#10. NAME PLACEHOLDERS
print("My name is {name} and I am {age} years old.".format(name="Bob",age=29))

#11. Formatting percentage
percent =0.876
print(f"Success rate is {percent:.2%}")

#12. Binary Format
num =5; print(f"Binary format is {num:b}")

#13. Hexadecimal 
print(f"Hexadecimal : {255:x}")

#14. Octal format
print(f"Octal : {255:o}")

#15. Exponential notation
big_num = 1234567; print(f"Scientific :{big_num:e}")

#16. Truncate Long text
long_text ="This is a long sentence";print(f"{long_text:.10}")

#17. Positional PlaceHolders
print("{0} {1} {0}".format("abra","cadabra"))

#18. Currency Formatting
amount = 45.678;print(f"Amount is :${amount:.2f}")

#19. Complex Sentence
user='Eve';points =950;print(f"User {user} has {points} points")

#20. Format with thousand seperator
num =123456789;print(f"Population: {num:,}")

#21.Multiple f-strings in one line
temp,humidity =28,70;print(f"Temperature is {temp}oC ,Humidity: {humidity}")

#22. Print Boolean Values
is_active =True;print(f"Active :{is_active}")

#23. Format to include quotes
word ='amazing';print(f"This is an '{word}' example.")

#24. Record Placeholders 
print("{2} {1} {0}".format("A","B","C"))

#25. CHAINED F-STRING
SUBTOTAL,TAX=100,0.15
print(f"Total : ${SUBTOTAL+SUBTOTAL*TAX:.2f}")


