"""
STUDENT RECORD

Input student details:
Name (string)
Roll Number (string/integer)
Age (integer)
Courses (store as a tuple)
Marks (store as a dictionary — subject as key, marks as value)


"""
print("Welcome to Student Program in Python")
student_details =[]
if len(student_details)==0:
    student_details =input("Enter student Details : Name  Roll Age ").split()
    #print(student_details)
    
while len(student_details)!=3:
    print("Enter Valid Details")
    break
#student_details =input("Enter student Details : Name  Roll Age ").split()
name = student_details[0];roll_no =int(student_details[1]) ;age=int(student_details[2])
print("Enter Course Details ")
courses = tuple(input("Enter Courses ").split())
print(courses)
marks = tuple(input("Enter Marks ").split())
##print(marks)

marks_dict = dict(zip(courses,marks)) ;  #print(marks_dict)

print("*"*50)
"""


DISPLAY ALL STUDENTS RECORDS

Show a summary of all student records.
Display Name, Roll No, Age, Courses, Marks, Average Marks, and Grade. 

"""
print("Displaying Records")
print(f"Student Name: {name}");print(f"Student Age :{age}");print(f"Student Roll_No: {roll_no}")
print(f"Student Courses :{courses}")
print(f"Student Marks :{marks_dict}")


"""
3️⃣ Search Student by Roll Number
Allow the user to enter a roll number.
Display all details of the corresponding student (if found).

"""
search_input = input("Do you want to search roll no \nEnter True or False")

if search_input== True:
    n = int(input("Enter Roll No :"))
    if roll_no==n:
        print("Student Found!")
        print(f"Student Name: {name}")
        print(f"Student Age :{age}")
        print(f"Student Roll_No: {roll_no}")
        print(f"Student Courses :{courses}")
        print(f"Student Marks :{marks_dict}")
    
    else:
        print("Student not Found")
else:
    print("Continuing to next step")
    
"""
4️⃣ Update Student Record
Modify student marks or details using their roll number.
Prompt for updated values (courses or marks).
1. Yes/ No
2. options: Details or Marks
3. Details get updated based on options
4. Marks get updated based on options
"""
answer =bool(input("Do you want to update student records: True/False "))
if answer == True:
    print("Updating Student Record")
    n = int(input("Enter Student roll no:"))
    if roll_no==n:
        strut=int(input("What do you want to update: \n1. Details \n2.Marks \nEnter 1 or 2 "))
        if strut==1:
            strut_details = input("Options \n1.Name \n2.Age  \n3. Roll_no  \nEnter 1 or 2 or 3")
            if strut_details ==1:
                name = input("Enter details for Name")
                print("Name Modified")
            elif strut_details ==2:
                age =int(input("Enter age"))
                print("Age modified")
            elif strut_details ==3:
                roll_no==int(input("Enter Student Roll No"))
                print("Roll number updated")
                
        elif strut==2:
            print("Subjects Available")
            for ele in marks_dict.keys():
                print(ele)
            sub = input("Enter Subject you want to change ")
            if sub in marks_dict:
                print("Key found")
                vv = int(input(f"Enter the marks for {sub} "))
                marks_dict[sub]=vv
                print("Marks Updated")
    else:
        print("Roll no doesn't exists")
else:
    print("Don't want to updated")
    
    
"""
5. Show average for students
"""

#marks_dict
""" courses1 =('Maths','English');marks1=(87,79)
marks_dict1 = dict(zip(courses1,marks1))  #
print(marks_dict1)
values11 = list(marks_dict1.values());print(values11) 
"""
print(f"Average for {name}")
for ele in marks_dict.items():
    print(f"{ele[0]} :{ele[1]}")
values11 = list(marks_dict.values())  #print(values11)
average_students = sum(values11)/len(values11)
print(f"Average of {name} :{average_students}")
      

"""
6. Delete Student Record
Remove a student record using the roll number.

"""

abc = 454564
#del abc;print(abc)
option_5 =bool(input("Option 5: Do you want to delete student record"))
if option_5 == True:
    aa_5 = int(input("Enter Roll No"))
    if aa_5 ==roll_no:
        print("Deleting student record")
        del name;del roll_no;del age;  #details deleted
        del courses;del marks; del marks_dict #course and marks deleted
        print("Details Deleted")
    else:
        print("Record doesn't exists")
else:
    print("Continuing to next step")
        
        

    
    

        
        

    

