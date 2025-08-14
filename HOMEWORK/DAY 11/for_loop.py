"""
FOR LOOP
QUESTIONS

"""

#1. Print days of the week
days =['Monday','Tuesday','Wed','Thursday','Friday','Saturday','Sunday']
for ele in days:
    print(ele)
    
#2. Print characters in a password
password ="Secret12345"
for ele in password:
    print("*",end=" ")
    
    
#3. CountDown Timer
for i in range(10,0,-1):
    print(f"Time Left: {i}")
    
    
#4. Print 1st 10 square numbers

for i in range(1,11):
    print(f"Square of {i} is {i**2}")
    

#5. Print top 5 movie names
movies =['Inception','Avatar','Titanic','GodFather','Salt']

for i in range(len(movies)):
    print(f"Movie no {i+1} : {movies[i]}")
    
    
#6. Loop over ID's order
order_ids =[101,102,103,104,105]
for ele in order_ids:
    print(ele)
    
    
#7. Loop to show employees salary
salaries =[30000,45000,60000,65645,354545]
i = 1
for ele in salaries:
    print(f"Salary of employee {i} : {ele} ")
    i+=1
    
    
#8. Loop through class roll numbers
for i in range(1,11):
    print(f"Roll no: {i}")
    
    
#10. Loop through month numbers
for month in range(1,13):
    print(f"Month is {month}")
    

#12. Print all vowels in string
text ='application'

for i in text:
    if i in 'aeiou':
        print("Vowel : ",i)
        
        
#13. Loop over emails 
emails =['a@gmail.com','b@yahoo.com','c@outlook.com']

for ele in emails:
    if '@' in ele:
        print(f"{ele} is a valid email")
        
        

        
    