# class Mobile:
#     def __init__(self, m):
#         self.model = m

#     def show_model(self, p):
#         self.price = p
#         print("Model:", self.model, "Price", self.price)
# realme = Mobile('RealMe X')
# realme.show_model(10000)
# print(id(realme))
# print()

# redme = Mobile('Redmi 7s')
# redme.show_model(3000)
# print(id(redme))
# print()


# newmobile = Mobile('New Mobile')
# newmobile.show_model(50000)
# print(id(newmobile))


# print(realme.price)
# print(realme.show_mode)


class Army:
    def __init__(self):
        self.name= 'Rashid'
        self.gn = self.Gun()

    def show(self):
        print("Name: ", self.name)
    class Gun:
        def __init__(self):
            self.name = 'AK47'
            self.capacity = '75 Rounds'
            self.length = '34.3 In'
        def disp(self):
            print("Gun name:", self.name)
            print("Capacity :", self.capacity)
            print("Lenghth :", self.length)


a = Army()
print(a.name)
a.show()
g = a.gn

print(g.name)
print(g.capacity)
print(g.length)

