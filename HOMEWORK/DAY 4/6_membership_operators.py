"""
MEMEBERSHIP OPERATORS

(IN , NOT IN)

"""

#1. Check if item exists in list

fruits =['apple','banana']
if 'banana' in fruits:
    print("There")
    
#2. Check if char in string
word ='Python'
if 'y' in word:
    print("Yes")
    

#3. Check if value not in set
roll_numbers ={101,102,103}
if 105 not in roll_numbers:
    print("Absent")
    
#4. Keyword in Sentence 
sentence = 'Python is awesome'
if 'awesome' in sentence:
    print("Present")
    
    
#5. Check file extension
filename ="report.pdf"
if '.pdf' in filename:
    print("PDF FILE")
    
    
#6. Check Domain
email ='user@gmail.com'

if '@gmail.com' in email:
    print("Gmail User")
    
    
#7. Character in Password
password ="myp@ass123"
if '@' in password:
    print("Valid special characters")
    
    
#8. Membership Operators in dict
student ={'name':'Raj','age':21}
if 'name' in student:
    print("Name exists")
    
#9. Memebership Values

if 21 in student.values():
    print("Age exists")
    
#10. Tuple
colors =('red','green','blue')
if 'blue' in colors:
    print("Present")
    
    
#11. Check in list of dicts
users =[{'id':1},{'id':2}]
if {'id':2} in users:
    print("Found")
    
    
#12. Find substring
msg ="Welcome to Python batch"
if 'Python' in msg:
    print()
    
#13. Word not in para
para ='Learning Python with real examples'
if "Java" not in para:
    print("Java is missing")
    
#14. Tag check in HTML
html="<h1> Hello <h1>"
if "<h1>" in html:
    print("Title tag found")
    
    
