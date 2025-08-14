"""
WHILE LOOP

"""

#1. ATM Pin Validation
pin =""
while pin !='1234':
    pin = input("Enter 4 digit pin")
    
    
#2. Wait for file to appear
import os
while not os.path.exists("data.txt"):
    print("Waiting for datafile")
    break

#3. Battery charging
battery = 10
while battery < 100:
    print(f"Battery charging at {battery}")
    battery+=10
    

#4. Alarm Clock Countdown
time_left = 5
while time_left >0:
    print("Alarm ringing in ",time_left)
    time_left -=1
    
    
#5. Waiting for exam result
result = None
while result is None:
    result =input("Enter resulr ?(yes/ no)")
    if result.lower()!='yes':
        result= None

print("Result Announced",result)


#6. Stock Price Monitor
price =100
while price <110:
    print(f"Current price stock: {price}")
    print("*"*30)
    price+=1
    
    
#7. Typing Race
target ='python'
typed =""
while typed!=target:
    typed = input("Type the word:python ")
    
    
#8. Repeat until odd number
num =2
while num %2 == 0:
    num = int(input("Enter odd number"))
    

#9. Wait until login success
logged_in = False
while not logged_in:
    user =input("Username ")
    pawd = input("Password ")
    if user=='admin' and pawd=='123':
        print("Welcome")
        logged_in =True
        
        
#10. Download Progress
progress = 0
while progress <=100:
    print(f"Downloding .................{progress}")
    progress +=20
    
#11. Game life simulation
lives = 3
while lives >0:
    print(f"You have {lives} lives")
    lives-=1
    

#12 Water boiling si



    

    