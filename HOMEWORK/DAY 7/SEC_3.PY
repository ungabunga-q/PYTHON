"""
ACCESSING TUPLE

"""

# 1.Access middle tuple
colors =('Red','Green','Blue','Yellow','Pink')
print(colors[len(colors)//2])

#2. Access first and last character from tuple of strings
chars =('alpha','beta','gamma')
print(chars[0][0],chars[-1][-1])

#3 .Access full name from tuple
person =('Shalini','Verma')
print(f"Full Name: {person[0]}  {person[-1]}")

""" TRICKY"""

# 4. Get domain from email tuple
email_info =('abc@gmail.com',)
print(email_info[0].split('@')[1])

# 5.IteraTING USING LOOP

nums =(10,20,30)
i=0
while i<len(nums):
    print(nums[i])
    i+=1
    
# 6.Slice last three elements
months =('Jan','Feb','March','Apr','May','Jun')
print(months[-3:])

# 7.Reverse access using negative indexing
ALPHABETS = ('A','B','C','D','E')
print(ALPHABETS[-2])

# 8. Use slicing to get every second time :
data = ('a','b','c','d','e','f')

# 9.Combine access and format
info =('Shalini','Trainer','Python')
print(f" {info[0]} is an expert {info[1]} in {info[-1]}")

# 10.Access nested tuples
college =('Delhi University',('BBA','BCA'))
print(college[1][1])

#11. Access date from time stamp
timestamp =('13','July','2025','15:00')
print(f"Date is : {timestamp[0]}-{timestamp[1]}-{timestamp[-2]}")

#12. Print initials from the full name
name =('Rahul','Dev','Verma');initals = name[0][0] + name[1][0] + name[2][0]
print(initals)

# 13. Access part of address tuple
address =("123 Street","New Delhi","110001");print(address[1])

# 14. Access last element
info = ('item1','item2','item3')
print(info[-1])

# 15. Check if item exists and access
products =('Laptop','Tablet','Phone')
if 'Tablet' in products:
    print("Tablet found at index",products.index("Tablet"))
    
#16. Tuple in decision making

login_status =(True,)
if login_status:
    print(login_status[0])

# 17. Use the loop with the index
name =('Amit','Pooja','Kabir')

for i in range(len(name)):
    print(f" {i+1}. {name[i]}")
    

# 18. CONCATENATE AND ACCESS
x=("Hello",);y=("World",);z=x+y
print(z[1])

#19. Unpack and print one value
record=('XYZ',101,'Intern')
__,emp,_=record
print(emp)

#20. Count specific characters from a tuple of strings
words =("Apple",'Banana','Cherry')
count =[i.count('a') for i in words];print(count)
print(f"Count is a is : {sum(count)}")


#21. Access through function
def show_emp(emp):
    print(f"Employee Name: {emp[0]} | Department: {emp[1]}")
    
show_emp(('Shalini','IT'))


#22. Tuple through multiple slicing
s =('one','two','three','four')
print(s[1:4]);print(s[:-2]);print(s[::3])


#23. Tuple with days and access weekends
days =('Mon','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
weekend = days[-2:];print(weekend)


#24. Dynamic Indexing
i= int(input("Enter index 0-3"))
data =('INDIA','USA','UK','CANADA')
if 0<=i <len(data):
    print("You selected :",data[i])
else:
    print("Invalid Index")
    
#25. Tuple with real-world use
location =(28.6139,77.2090)
print(f"Latitude: {location[0]}, Longitude: {location[1]}")

