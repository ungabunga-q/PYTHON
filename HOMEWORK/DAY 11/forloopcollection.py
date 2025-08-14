"""
FOR 
LOOP
OVER
COLLECTIONS
(LISTS, TUPLES ,SET , DICTIONARY)

"""

#1. LOOP THROUGH STUDENT NAMES
students =['Anuj','Meera','Kabir']
for ele in students:
    print("Present : ",ele)
    
    
#2. Loop through tuple of temperatures
temps =(30.5,32.1,29.0,28.7)
for t in temps:
    print("Temp : ",t)
    
    
#3. Loop through a dictionary of book prices

books ={'Python':459,'c++':400,'Java':500}
for key,value in books.items():
    print(f"{key} : {value}")
    
    
for book,price in books.items():
    print(f"{book} : {price}")
    

#4. Loop through a shopping cart
cart_items ={'shoes','shirt','jeans'}
for item in cart_items:
    print("Cart contains : ",item)
    
    
#5. Loop through characters of password
password ='Mysecret'
#print(password[0])
for i in range(len(password)):
    print(f"Character {i} : {password[i]}")
    
for i in password:
    print("*",end="")
    
    
#6. Loop through bank accounts with balances

accounts  = {'AI101':500,'A102':12000,'A103':8000}

for acc,balance in accounts.items():
    print(f"Account {acc}: Balance : {balance}")
    
    
#7. Loop through a list of website urls
urls =['google.com','github.com','linkedin.com']
for ele in urls:
    print("Opening : ",ele)
    
    
#8. Loop through a tuple of subject scores

scores =(88,77,92,85)
for score in scores:
    print(f" Score :",score)
    
    
#9. Loop through dict to show employee departments
departments ={'Ram':'HR','Shyam':'IT','Geeta':'Finance'}
for emp,dept in departments.items():
    print(f"{emp} -> {dept}")
    

#10. Loop through a list 
phone ='9876543210'
for i in phone:
    print(i,end=" ")
    
    
#11.  Iterate over a set of countries
countries ={'India','USA','GERMANY','canada'}
print(countries)
for ele in countries:
    print(f"Visited : {ele}")
    
    
#12. Loop over names and print in uppercase
names =['ravi','komal','ishaan']
for ele in names:
    print(ele.upper())
    print(ele.capitalize())
    print(ele.lower())
    print("*"*50)
    
#13. Loop over dictionary keys
flight_schedule ={'Indigo':'9:00 am','Air India':'12:30 pm'}
for airline in flight_schedule:
    print(f"Flight : {airline} : {flight_schedule[airline]}")
    
    
#14. Loop through letters of a username
Username ='AlphaUser'
for ch in Username:
    print(ch)
    

#15. Loop through a mobile app icons list
apps =['Instagram','Facebook','Twitter']
for ele in apps:
    print(ele)
    
#16. Loop through a set of unique customer ids
customer_ids ={'C101','C102','C103'}
for ele in customer_ids:
    print(ele)
    
#17. Loop through a dictionary of student marks
students_marks ={'Aman':80,'Kirti':95,'Tina':89}
for student,marks in students_marks.items():
    print(f" {student} scored {marks}")    
    
#18. Groceries list
groceries ={'milk','eggs','bread','fruits'}
for ele in groceries:
    print("Buy : ",ele)
    
#19. Loop over tuple of login attempts

login_attempts =(1,2,3)
for attempt  in login_attempts:
    print(f"Attempt : ",attempt)
    

#20. Loop through the dict with nested list
students ={'Ravi':[70,80],'Kiran':[85,90]}
for name,marks in students.items():
    print(f"{name} -> {marks}")
    
    
#21. Loop over a brand names in set
brands ={'Nike','Addidas','Sketchers','Reebok'}
for brand in brands:
    print("Brand: ",brand)
    
    
#22. Loop over characters and count vowels
text ='application'
for ch in text:
    if ch.lower() in 'aeiou':
        print('Vowel Found',ch)

#23. Loop through employee dict and print initials

employees ={'Amit Kumar':'Hr','Sunita Jain':'Admin'}
for ele in employees:
    initals =''.join( ele[0] for ele in ele.split())
    print(initals)
    
    
for ele in employees:
    initals =[ ele[0] for ele in ele.split()]
    print(initals)
    

#24. Loop over data packages

dataplans =[1.5,2,3,5]
for plan in dataplans:
    print(f" {plan} GB plan available")

    
#25. Loop through a string to count digits
data = 'user123profile456'
for ele in data:
    if ele.isdigit():
        print("Digit : ",ele)
        

#26.  Loop through tags in social media posts
tags ={'#fitness','#workout','#goals'}
for tag in tags:
    print(f"Tag : {tag}")
    
    
#27. Loop through file extensions
extensions =['.jpg','.png','.pdf']
for ext in extensions:
    print(f"Supported Format : {ext}")
    
    
#28. Loop through subjects to mark attendance
subjects =['Maths','Science','English']
for ele in subjects:
    print(f"Subject : {ele}")
    
    
#29. Loop through a list of installed apps
installed_apps =['Zoom','Slack','Notion']
for ele in installed_apps:
    print(f"Launching : {ele}")
    
    
#30. Loop through a string and reverse it
name ='Shalini'
for ch in name:
    print(ch,end="")
    
for ch in reversed(name):
    print(ch,end="")
    
    
# Using Nested loopd in Python

#1. Print 2D MATRIX
matrix =[[1,2],[3,4],[5,6]]
for row in matrix:
    for col in row:
        print(col,end='')
    print()
    

#2. Print multiplication table (1,5)
for i in range(1,6):
    print(f"Multiplication table of {i} ")
    for j in range(1,11):
        print(f"{i} * {j} = {i*j} ")