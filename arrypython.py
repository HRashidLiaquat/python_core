from numpy import *
import numpy as np

# sturoll = array([101, 102, 103, 104, 105])

# n= len(sturoll)
# for i in range(n):
#     print(sturoll[i])

# a = np.array([101, 102, 103, 104, 105])
# b = np.array([101, 102, 103, 104, 105])


# c= a + b
# n = len(c)

# for i in range(n):
#     print(c[i])
# i = 0
# while i<n:
#     print(i, "Index", "=" , sturoll[i])
#     i+=1


# d = np.array([1, 2, 3, 4, 5, 6])
# e = np.array([2, 4, 6, 8, 10, 12])

# f = d == e

# print(f)


# a = np.array([100, 200, 300, 40, 50, 51])
# b = np.array([2, 5000, 2, 60000, 1, 0])

# result = where(a>b, a, b)

# print(result)




# a = np.array([1, 2 ,3 ,0])

# result = nonzero(a)
# print(result)


# n = int(input("Enter number of element: "))
# a = zeros(n, dtype=int)
# print(a)

# for i in range(len(a)):
#     x= int(input("Enter the Element: "))
#     a[i] = x
# for i in range(len(a)):
#     print(a[i])


# n = int(input("Enter numbers of elements:"))
# a = zeros(n, dtype=int)
# u = len(a)
# i = 0
# j = 0

# while i< u:
#     x = int(input("Enter Elements:"))
#     a[i] = x
#     i+=1
# while j< len(a):
#     print(a[j])
#     j+=1

# a = np.array([[10, 20, 30, 40], [50, 60, 70, 80]], dtype=int)
# print(a.dtype)
# print(a[0][0])
# print(a[0][1])
# print(a[0][2])
# print(a[0][3])
# print(a[1][0])
# print(a[1][1])
# print(a[1][2])
# print(a[1][3])

# st = np.array([["Rahula","Sonam","Raj","Rani"],["Dell","Asus","Lenovo","HP"]])
# print(st.dtype)
# print(st[0][0])
# print(st[0][1])
# print(st[0][2])
# print(st[0][3])
# print(st[1][0])
# print(st[1][1])
# print(st[1][2])
# print(st[1][3])


# a = np.array([[10, 20, 30, 40], [50, 60, 70, 80]], dtype=int)

# a[1][2] = 900000
# n = len(a)
# #Without index
# # for i in a:
# #     for c in i:
# #         print(c)
# #With index
# for i in range(n):
#     for c in range(len(a[i])):
#         print(a[i][c])
#     print()

# a = np.array([[10, 20, 30, 40], [50, 60, 70, 80]], dtype=int)

# n = len(a)
# i = 0

# while i <n:
#     j= 0
#     while j <len(a[i]):
#         print(a[i][j])
#         j+=1
#     i+=1




m = int(input("Enter number of row:"))
n = int(input("Enter Numbers of columns:"))

a = zeros((m,n), dtype=int)
u = len(a)
print(a)
for i in range(u):
    for j in range(len(a[i])):
        x = int(input("Enter Element: "))
        a[i][j] = x
for i in range(u):
    for j in range(len(a[i])):
        print(a[i][j])






