# class Laptop:
#     discount = 10
#     def __init__(self, brand, name, price):
#         self.brand = brand
#         self.name = name
#         self.price = price

#     def f_name(self):    ## it is method because def. inside class
#         return f"{self.brand} {self.name}"
#     def is_costly(self):  ## it describes budget segment or not
#         return self.price > 25000
#     def off_price(self):  ## it show how much is discount
#         v1 = (self.discount/100)*self.price
#         return self.price - v1

# l1 = Laptop('acer', 'aspire', 225000)
# l2 = Laptop('hp', 'povelion', 110000)
# l1.discount = 80

# print(l1.price)
# print(l2.name)
# print(l2.brand)
# print(l2.f_name())
# print(l2.is_costly())
# print(l1.off_price())
# print(l2.__dict__)


# class Circle:
#     pi = 3.14  ## it is called as class variable 
#     def __init__(self, radius):
#         self.r = radius
#     def circum(self):
#         return 2*Circle.pi*self.r

# c1 = Circle(5)

# print(c1.circum())

class Person:  ## for counting no. of instances
    count = 0
    def __init__(self, fname, lname, age):
        Person.count += 1
        self.f = fname
        self.l = lname
        self.age = age

        
p1 = Person('h', 'v', 24)
p2 = Person('h', 'v', 24)
p3 = Person('h', 'v', 24)
p1 = Person('h', 'v', 24)


print(Person.count)


