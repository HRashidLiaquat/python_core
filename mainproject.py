# import calculation
# import Admin.user
# import Product.p_cat
# import services.serviceses

from abc import ABC, abstractmethod


class Father(ABC):

    @abstractmethod
    def create_product(self):
        pass
    def create_service(self):
        print("Concreate Method")

class child(Father):
    def create_product(self):
        print("Child Class")
        print("Defining Abstract Method")
c = child()
c.create_product()
c.create_service()


class DefenceForce(ABC):

    @abstractmethod
    def area(self):
        pass
    def gun(self):
        print("Gun = AK-47 Rifle")

class Army(DefenceForce):
    def area(self):
        print("Area = Land")
class Navy(DefenceForce):
    def area(self):
        print("Area = Sea")
class AirForce(DefenceForce):
    def area(self):
        print("Area = Air")


a = Army()
a.area()
a.gun()

print("-----")
n = Navy()
n.area()
n.gun()
print("-----")
af = AirForce()
af.area()
af.gun()








# print("Cal Module's Name:", calculation.name)

# print("Cal Module's Variable:", calculation.a)

# calculation.name()

# a = calculation.add(10, 20)
# print(a)


# b =calculation.sub(10,20)
# print(b)

# print(Admin.user.usser())
# print(Product.p_cat.producat())
# print(services.serviceses.servicess_addproducat())

