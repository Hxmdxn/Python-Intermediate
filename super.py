class New: #parent class
    def __init__(myobj,Phone,Price):
        myobj.Phone=Phone
        myobj.Price=Price

    def myfunc(self):
        print("Name - ",self.Phone,"Price - ",self.Price)

p2=New("Samsung",50000)   
p2.myfunc()     

class New2(New): #child class
    def __init__(myobj,Phone,price,year):
        super().__init__(Phone,price) #attributes of method of parent class and no need of self
        myobj.year=year #adding parameter to child class

    def myfunc2(self): #adding method to child class
        print("Name - ",self.Phone,"Price - ",self.Price,"Year - ",self.year)

p6=New2("IPhone",60000,2022)
p6.myfunc2()

#to add value
# class New2(New):
#     def __init__(self,name,place):
#         super().__init__(name,place)
#         self.year=2019
#     def fn2(self):
#         print("Name is ",self.name,"Place is : ",self.place,self.year)
# p1=New2("Ameen","UK")
# p1.fn2()