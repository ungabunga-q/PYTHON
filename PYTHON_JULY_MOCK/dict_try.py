
courses =('Maths','English');marks=(87,79)
marks_dict = dict(zip(courses,marks))  #
print(marks_dict)

values11 = list(marks_dict.values())
print(sum(values11))

for ele in marks_dict.items():
    print(f"{ele[0]} :{ele[1]}")
    

print("Subjects Available")
for ele in marks_dict.keys():
    print(ele)
sub = input("Enter Subject you want to change ")
if sub in marks_dict:
    print("Key found")
    vv = int(input(f"Enter the marks for {sub} "))
    marks_dict[sub]=vv
    print("Marks Updated")
    
print(marks_dict)


