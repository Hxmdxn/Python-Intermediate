#POLYMORPHISM (same module name)
class Car:
    def __init__(self,carname):
        self.carname=carname
    def access(self):
        print("DRIVE")

class Ship:
    def __init__(self,shipname):
        self.shipname=shipname
    def access(self):
        print("SAIL")

class Plane:
    def __init__(self,planename):
        self.planename=planename
    def access(self):
        print("FLY")

#objects together
d=Car("Mustang")
s=Ship("Titanic")
p=Plane("Boeing")

for x in (d,s,p):
    x.access()

        