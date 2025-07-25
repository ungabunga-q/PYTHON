"""
LOGICAL OPERATORS

{AND, OR , NOT}

"""

#1. Check if the person is adult and has voter id

age = 22; has_voter_id= True
if age>=18 and has_voter_id:
    print("Eligible to vote")
    

#2. Student Eligible for scholarship
marks = 85;income=20000
if marks > 80 and income <=25000:
    print("Eligible for scholarship")
    
    
#3. Login check using OR
has_email = False;has_phone =True
if has_email or has_phone:
    print("Person can login")
    
#4. Not operator usage
is_logged_in = False
if not is_logged_in:
    print("Please login first")
    
#5. Check if weekday or weekend
weekend= True;holiday = False
if weekend or holiday:
    print("Today is Holiday")



#14. Multiple Login Options
login_google= True
login_facebook= False
login_github = True

if login_google or login_facebook or login_github:
    print("User logged in")
    
    
#24. Battery charging check
is_plugged = True;battery_percentage=45
if is_plugged and battery_percentage <=100:
    print(f"Charging ...............")