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