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
p6.myfunc()


