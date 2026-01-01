import calculation
import Admin.user
import Product.p_cat
import services.serviceses





print("Cal Module's Name:", calculation.name)

print("Cal Module's Variable:", calculation.a)

calculation.name()

a = calculation.add(10, 20)
print(a)


b =calculation.sub(10,20)
print(b)

print(Admin.user.usser())
print(Product.p_cat.producat())
print(services.serviceses.servicess_addproducat())

