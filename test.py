print("Rashid Liaquat");

# Variables
# name = "Rashid Liaquat"
# age = 30
# print(f"Name: {name}, Age: {age}")
# # Data Types
# is_student = False  
# height = 5.9  


# Lists

data = [1, 2, 3, 4, 5,'Rashid Liaquat']

print("Data List:", data[1])
print("Data List:", data[-1])
print("Data List Length:", len(data))



#Tuples

data1= (10, 20, 30, 40, 50,'Rashid Liaquat')
print("Data1 Tuple:", data1[2])
print("Data1 Tuple Length:", len(data1))
print("Data1 Tuple:", data1[-1])


rg = range(5)
print("Range:", list(rg))
print("Range Length:", len(rg))
print("Range Start:", rg.start)
print("Range Stop:", rg.stop)
print("Range Step:", rg.step)
print("Range Element at Index 2:", rg[2])
print("Range Element at Index -1:", rg[-1])
print("Range Sliced (1 to 4):", list(rg[1:4]))
print("Range Sliced (0 to 5 with step 2):", list(rg[0:5:2]))



# Sets
#Set is a collection which is unordered, unchangeable*, and unindexed.
sets2 = {1, 2, 3, 4, 5,'Rashid Liaquat'}
print("Data2 Set:", sets2)

# Dictionaries
#Dictionaries are used to store data values in key:value pairs.
data5 = {'name': 'Rashid Liaquat', 'age': 30, 'is_student': False}
print("Data5 Dictionary:", data5['name'])
print("Data5 Dictionary:", data5)

type(data5)
print("Data5 Type:", type(data5))

#Operators
a = 10
b = 5
sum_result = a + b
print("Sum:", sum_result)
diff_result = a - b
print("Difference:", diff_result)
prod_result = a * b
print("Product:", prod_result)
div_result = a / b
print("Division:", div_result)
mod_result = a % b
print("Modulus:", mod_result)
exp_result = a ** b
print("Exponentiation:", exp_result)
floor_div_result = a // b
print("Floor Division:", floor_div_result)

#Relational Operators
#Relational operators are used to compare two values.

a = 2
b = 10
print("a == b:", a == b) # False
print("a != b:", a != b) # True   
print("a > b:", a > b) # False
print("a < b:", a < b) # True   
print("a >= b:", a >= b) # False
print("a <= b:", a <= b) # True
#Logical Operators
#Logical operators are used to combine conditional statements.
x = 5
print("x > 3 and x < 10:", x > 3 and x < 10) # True
print("x > 3 or x < 4:", x > 3 or x < 4) # True
print("not(x > 3 and x < 10):", not(x > 3 and x < 10)) # False

x1 = 1;
y1 = 2;

print(x1==1 and y1!=2) # False
print(x1==1 or y1!=2)  # True
print(x1!=1 or y1==2)  # True
print(not(x1==1 and y1==2)) # False
print(not(x1==1 or y1!=2))  # False

