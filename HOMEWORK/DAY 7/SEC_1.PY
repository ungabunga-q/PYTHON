""" 
SECTION 1 : DEFINING TUPLE

"""

#1. TUPLE OF 5 ODD NUMBERS
odds = (1,3,5,7,9);print(odds)

#2. tuples with different currencies
currencies =('inr','USD','EUR','JPY');print(currencies)

#3. Tuple of names
names = ("Amit","Zara","Zoya","Rahul");print(names)

#4. from input age
age = int(input("Enter your age?"))
use_info = ("User",age)
print(use_info)

#5. Tuple with Square numbers
squares = (1*1,2*2,3*3,4*4,5*5);print(squares)

#6. Tuple storing one variable
one_value = ("Data",);print(one_value)

#7. Tuple of ASCII VALUES 
ascii_values = (ord('A'),ord('B'),ord('C'));print(ascii_values)


#8. Tuple of mixed Sports
sports = ("Cricket","Football","Basketball");print(sports)

#9. Tuple of planets
planets =("Mercury","Venus","Earth","Mars");print(planets)


#10. Temperature readings
temp_readings =(28.3,30,25.6,30.1);print(temp_readings)

#11. Tuple with Python keywords
keywords = ("if","else","while","for");print(keywords)

#12. Tuple of even numbers
even_numbers = tuple(range(2,13,2));print(even_numbers)

#13. Tuple from split string
sentence ="Python is Fun";words =tuple(sentence.split())
print(words)

#14. Tuple with formatted strings
import sys
print(sys.version)
version =(f"Python version is {sys.version}")
print(version)

#15. Tuple with mobile brands
m_brands =("Xiomi","Redmi","Apple","Samsung","One Plus");print(m_brands)

#16. Tuple with Boolean conditions
results = (5>3,2==4,not False);print(results)

#17. Tuple of prime numbers
list1 =[2,3,5]

for i in range(2,20):
    if i%2!=0 and i%3!=0 and i%5!=0:
        list1.append(i) 
print(list1)


#18. Currency conversions
rates =(83.25,0.91,110.0);print(rates)

#19. Tuple of city names
cities =("Mumbai","Delhi","Kolkata","Chennai");print(cities)

#20. Tuple from characters
chars = tuple("DATA");print(chars)

#21.TUPLE WITH AGE GROUPS
age_groups=("0-10","11-18","19-30","31-50","50+")
print(age_groups)

#22. Tuple of colour shades
shades =("LIGHT GREEN","DARK GREEN","BRIGHT RED");print(shades)


#23. Tuple with input values from multiple formats
name =input("Enter your name");score = int(input("Enter your score"))
result = (name,score);print(score)