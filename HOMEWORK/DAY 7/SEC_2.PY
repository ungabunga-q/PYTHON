""" 
2. CREATING A TUPLE

"""

#1. Tuple from a list of subjects
subjects =['english','history','maths'];
subjects_tuple =tuple(subjects)
print(subjects_tuple)

#2. Tuple from a list of marks
marks_list =[80,90,88];marks_tuple = tuple(marks_list)
print(marks_tuple)

#3. Tuple from input string
data = tuple(input("Enter the name:"));print(data)


"""4th not done
"""

#5. Tuple from a range of 1 to 5
tuple_RANGE = tuple(range(1,6));print(tuple_RANGE)

#6.Tuple from boolean results
values =[True,False,True];bool_tuple=tuple(values)
print(bool_tuple)


#7. Tuple from float numbers
floats =[1.4,5.3545,6.24,9.34];float_tuple=tuple(floats)
print(float_tuple)

#8. Tuple using multiplication
mul_tu = tuple([(i,i*2) for i in range(1,100,4)])
print(mul_tu)

#9. Tuple from a list of characters
char_list = list("HELLO");char_tuple =tuple(char_list)
print(char_tuple)

#10. Tuple of coordinates

""" import requests

res = requests.get("https://ipinfo.io/json")
data = res.json()
lat, lon = data["loc"].split(",")
print("Latitude:", lat)
print("Longitude:", lon)

coordinates =(lat,lon);print(coordinates) """

""" 11th didn't do """

#12. Tuple using slicing
lst =[i for i in range (10,51,10)];print(lst)
tuple_slicing = tuple(lst[1:4]);print(tuple_slicing)


#13. Tuple from input converted list
items = input("Enter 3 items comma seperated.split").split(",")
print(items)
items_tuple = tuple(items);print(items_tuple)

#14. Tuple from square roots
import math
roots =[ math.sqrt(x) for x in [4,9,16,25,36,49,64,81,100]];roots_tuple = tuple(roots)
print(roots_tuple)


#15. Tuple from binary string
bin_tuple = tuple([ bin(i)[2:] for i in range (1,51,3)])
print(bin_tuple)

#16. Tuple from reversed list



 
#24. Tuple from string formatting
name= "Shalini";tp1=(f"Welcome {name}",);print(tp1)
 
 

