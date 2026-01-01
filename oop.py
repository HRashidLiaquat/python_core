class Mobile:
    def __init__(self, m):
        self.model = m

    def show_model(self, p):
        self.price = p
        print("Model:", self.model, "Price", self.price)
realme = Mobile('RealMe X')
realme.show_model(10000)
print(id(realme))
print()

redme = Mobile('Redmi 7s')
redme.show_model(3000)
print(id(redme))
print()


newmobile = Mobile('New Mobile')
newmobile.show_model(50000)
print(id(newmobile))


# print(realme.price)
# print(realme.show_mode)

