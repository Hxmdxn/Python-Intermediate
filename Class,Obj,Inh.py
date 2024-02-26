class MyClass: #AOa
    x=5 #prop/attribute
p1=MyClass() #object/instance
print(p1.x) #to access the attribute

class New: 
    x=15
    y=25
p2=New()
print(p2.x,p2.y)

#__init__ function  
class MyClass:
    def __init__(self,name,place,age):
        self.name=name
        self.age=age
        self.place=place
p1=MyClass("John","India",30) 
print(p1.name)
print(p1.place)
print(p1.age)

#Q) Create a class named person , use __init__ to assign values for place and house number
class Person:
    def __init__(self,place,houseno):
        self.place=place
        self.houseno=houseno
        
p3=Person("India",33)
print(p3.place,p3.houseno)

#__str__ function
class Person:
    def __init__(self,name,place,age):
        self.name=name
        self.place=place
        self.age=age 
    def __str__(self):
        return f"{self.name}{self.place}({self.age})" #specifier used.
p4=Person("Hamdan "," India ",20)
print(p4)

#Q)create a class and object to print the job and salary using str() fn.
class Test:
    def __init__(self,job,salary):
        self.job=job
        self.salary=salary
    def __str__(self):
        return f"{self.job}{self.salary}"
p=Test("Developer ",600000)
print(p)

#Object Methods
class New:
    def __init__(myobj,name,age):
        myobj.name=name
        myobj.age=age
    def myfunc(example): #method
        print("I'm",example.age,"Years old")
        
p5=New("Hamdan",20)
p5.age=30 #modifying values
print(p5.age)

#create a class and object also contain methods to print the dress and its price
class Shop:
    def __init__(self,dress,price):
        self.dress=dress
        self.price=price
    def myfunc(self):
        print("Product is ",self.dress,",Price =",self.price)
        
pp=Shop("Shirt",2500)
pp.myfunc()

#Q) Create a class and object to print the name and address of a person.

class Person:
    def __init__(self,Name,address):
        self.Name=Name
        self.address=address
    def myfunc(self):
        print("NAME- ",self.Name," ADDRESS - ",self.address)
        
p=Person("Hamdan","Angadipuram")
p.myfunc()

#Q) create a class and object to print the phone and its price

class New:
    def __init__(myobj,Phone,Price):
        myobj.Phone=Phone
        myobj.Price=Price
    def myfunc(self):
        print("Name - ",self.Phone,", Price -",self.Price)

p6=New("IPhone",60000)
p6.Price=55000 #modifying values
p6.myfunc()

# #deleting a prop inside object
# class New:
#     def __init__(myobj,Phone,Price):
#         myobj.Phone=Phone
#         myobj.Price=Price
#     def myfunc(self):
#         print("Name - ",self.Phone,"Price -",self.Price)

# p6=New("IPhone",60000)
# print(p6.Phone,p6.Price)
# del p6.Price #syntax
# print(p6.Price) #will return error

# # #deleting an object
# class New:
#     def __init__(myobj,Phone,Price):
#         myobj.Phone=Phone
#         myobj.Price=Price
#     def myfunc(self):
#         print("Name - ",self.Phone,"Price -",self.Price)

# p6=New("IPhone",60000)
# del p6
# print(p6)

#pass statement 
class person:
    pass #to avoid error

#Inheritance
#class inside another class
class New: #parent class
    def __init__(myobj,Phone,Price):
        myobj.Phone=Phone
        myobj.Price=Price
    def myfunc(self):
        print("Name - ",self.Phone,"Price -",self.Price)
        
class New2(New): #child class
    def __init__(myobj,Phone,price):
        New.__init__(myobj,Phone,price) #assigning to parent

p6=New2("IPhone",60000)
p6.myfunc()#add the text as well


