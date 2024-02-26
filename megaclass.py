#Car Representation
class Car:
    def __init__(self,make,model,year,price,condition):
        self.make=make
        self.model=model
        self.year=year
        self.price=price
        self.condition=condition
    def __str__(self):
        return f"{self.make}{self.model}{self.year}{self.price}{self.condition}"
    
    def myfunc(self):
        print("Name of car : ",self.make," Model - ",self.model,"Price - ",self.price,
              "Year - ",self.year,
              "Condition - ",self.condition)

class Car2(Car):
    def __init__(self,make,model,year,price,condition):
        Car.__init__(self,make,model,year,price,condition)

    
    def myfunc2(self):
        print("Name of car : ",self.make," Model - ",self.model,"Price - ",self.price,
              "Year - ",self.year,
              "Condition - ",self.condition)
class Car3(Car):
    pass

class Car4(Car):
    def __init__(self,make,model,year,price,condition):
        super().__init__(make,model,year,price,condition)
    

print("Car 1")
p1=Car("TOYOTA","Camry",2008,25000,"Excellent")
p1.myfunc()

print("Car 2")
p2=Car2("Honda","Civic",2010,25600,"Excellent")
print(p2.make)
p2.myfunc()

print("Car 3")
p3=Car2("SUZUKI","Spresso",2023,50000,"Good")
print(p3.make,p3.model,p3.price,p3.year,p3.condition)
p3.myfunc()

print("Car 4")
p4=Car("Maruti","Alto",2023,50000,"Excellent")
p4.make="TATA" #modifying
p4.myfunc()
p4.price=55000 #modifying
p4.myfunc()


