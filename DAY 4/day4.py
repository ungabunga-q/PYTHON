# ============================================
# 4. LOGICAL OPERATORD
# AND ,OR , NOT

age = 20; has_id = True
print(age >=18 and has_id) #true

username ="admin";password ="123"
print(username=="admin" or password=="admin") # true

is_busy =False ; print(not is_busy)

grade ="A"; attendance =90
print(grade == 'A' and attendance>85)

income =30000; credit_score = 750
print(income >25000 and credit_score >=700) # true

height = 150 ;age = 12 
print(height >=140 and age >=10)

total_amount = 400; coupon = True
print(total_amount > 500 or coupon)  #true

msg = ""; print(not msg)



print(age >=18 and has_id)  # driving license

is_weekend = True ;is_holiday = False
print(is_holiday or is_weekend)

# ============================================
# 5. BITWISE OPERATORS
# &,|,^,~,<<,>>

""" GET BINARY NUMBER
-------------------- 512,256,128,64,32,16,8,4,2,1

Binary of 5 is -101
Binary of 3 is -0011


"""

a = 5; b =3  #0101 ; #0011
print(a & b) # and : 1
print(a | b) # or : 7
print(a ^ b) # xor : 6
print(~ a) # not : -6
print( a<<1) # left shift : 10
print(a>>1) # right shift : 2

read = 4
write = 2
execute = 1
user = read | write #6. ( read +write)
print(user)

x = 7 #0111
mask = ~1
print(x & mask)  #turn of last bit :6

num = 4
print(num & 1 ==0)  # even check : True

# Efficient calculations ( swapping without temp variables)
x = 10;y =20
temp = x; x=y; y= temp;
print(x,y)
print(x,y)
x,y=y,x
print(x,y)

x = x^y;y=x ^y ;x=x^y;
print(x,y)

"""
Flags and permissions (Access control systems)
Imagine managing user permissions like:

read = 1
write = 2
execute = 4

    """
    
# Example : Asssign and check user access
# user has read + execute
user_permission = 1|4 #5
print(user_permission)

# Check if the user has write access
has_write = user_permission & 2
print(has_write)
print("Write Access :",bool(has_write))

# add write access
user_permission |=2 # now permission is 7
print(f"Updated user :{user_permission}")

# =========================
# 6. MEMBERSHIP OPERATORS
# in ,not in


fruits =["apple","banana","grape"]
print("apple" in fruits) # true
print("orange" not in fruits) # true

email = "shalini@example.com"
print("@" in email) #valid email check

text = "Python is powerful"
print("Python" in text)

usernames =['admin','text']
print("admin" in usernames)

print("a" in "data")

permissions ="rw"
print("r" in permissions and "w" in permissions)

banned =["abc","xyz"]
print("user1" not in banned)

courses = ["Python","Java"]
print("Python" in courses)

coupon_codes =[ "SAVE50","NEW100"]
print("SAVE50" in coupon_codes)

