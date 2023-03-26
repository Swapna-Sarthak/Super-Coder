'''
class Vehical:
    def __init__(self, id1,type1,cost):
        self.__id1 = id1
        self.__type1 = type1
        self.__cost = cost
        self.__prem = None
    def purchase(self,__cost):
        if (self.__type1 == "Two wheeler"):
            self.__prem = self.__cost*0.02
        elif(self.__type1 == "Four wheeler"):
            self.__prem = self.__cost*0.06
    def display(self):
        print("car id",self.__id1)
        print("car type",self.__type1)
        print("car cost",self.__cost)
        print("car premium cost",self.__prem)
    def get_1(self):#get is used to get data from private object instances
        return self.__id1
    def set_1(self,new_id):
        self.__id1=new_id
vh1=input("Enter car type")
if(vh1 not in ["Two wheeler","Four wheeler"]):
    print("Invalid input")
    exit()
vcost=int(input("Enter the car price"))
vid=input("Enter the car id")
obj1=Vehical(vid,vh1,vcost)
obj1.purchase(vcost)
obj1.display()
print(obj1.get_1())
obj1.set_1("OR34H6868")
print(obj1.get_1())
'''
#####################################################################
'''
class Student:
    def __init__(self, id1,age,mark):
        self.__id1 = id1
        self.__age = age
        self.__mark = mark
        self.__accept= None
    def validate_age(self):
        if(self.__age >= 20):
            return True
        else:
            return False
    def validate_mark(self):
        if(mark not in range(0,101)):
           return False
        elif(mark > 65):
            return True
    def check_qualification(self):
        if(obj1.validate_age() and obj1.validate_mark()):
            return True
        else:
            return False
    def get_id(self):
        return self.__id1
    def set_id(self,new_id):
         self.__id1=new_id
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        self.__age=new_age
    def get_mark(self):
        return self.__mark
    def set_mark(self,new_mark):
        self.__mark=new_mark
id1=int(input("Enter The ID"))
age=int(input("Enter Your Age"))
mark=int(input("Enter Your Mark"))
obj1=Student(id1,age,mark)
if(obj1.check_qualification()):
    print("Congratulations!!! You Passed")
    cid=int(input("Enter a course id"))
    if(cid==1001):
        if(obj1.get_mark()>= 85):
            fees=25575-(25575*0.25)
        else:
            fees=25575
        print("Fees to be paid:",fees)
    elif(cid==1002):
        if(obj1.get_mark()>= 85):
            fees=15500-(15500*0.25)
        else:
            fees=15500
        print("Fees to be paid:",fees)
    else:
        print("Invalid Course ID")
        
else:
    print("Better Luck Next Time")
    id1=int(input("Reenter The ID"))
    age=int(input("Reenter Your Age"))
    mark=int(input("Reenter Your Mark"))
    obj1.set_id(id1)
    obj1.set_age(age)
    obj1.set_mark(mark)
'''
######################################################################
class PizzaForYou:
    def validate_pizza_size(self):
        if(self.size not in ["Small","Medium"]):
            return False
        else:
            return True
    def cal_pizza_cost(self):
        if (obj1.validate_pizza_size()):
            if(self.size=="Small" and self.topping=="1" ):
                self.cost=(150*self.quantity)+(35*self.quantity)
            elif(self.size=="Small" and self.topping=="0"):
                self.cost=(150*self.quantity)
            elif(self.size=="Medium" and self.topping=="1" ):
                self.cost=(200*self.quantity)+(50*self.quantity)
            elif(self.size=="Medium" and self.topping=="0" ):
                self.cost=(200*self.quantity)
            else:
                print("Invalid input")
        return self.cost
class Customer(PizzaForYou):
    def __init__(self,size,quantity,topping):
        self.size=size
        self.quantity=quantity
        self.topping=topping
        self.cost=None
    def add_toppings(self):
        if(self.toppings!=0):
            return True
        else:
            return False
    def validate_quantity(self):
        if(self.quantity in range(1,6)):
            return True
        else:
            return False
    
class DoorDelivery:
    def __init__(self,size,quantity,topping,dist,cost):
        self.size=size
        self.quantity=quantity
        self.topping=topping
        self.dist=dist
        self.cost=cost
    def validate_delivery_dist(self):
        if(dist in range(1,11)):
            return True
        else:
            return False
    def pizza_cost(self):
        if(self.validate_delivery_dist()):
            for i in range(1,self.dist+1):
                if(self.dist<=5):
                    self.cost+=5
                if(self.dist>5 and self.dist<=10):
                    self.cost+=7
                    
                self.dist+=1
        return self.cost
size=input("Enter size of pizza")
quantity=int(input("Enter the number of pizza"))
topping=input("Enter 1 if topping nedded 0 if not")
dist=int(input("Enter distance"))
obj1=Customer(size,quantity,topping)
if(obj1.validate_quantity()):
    obj1.cal_pizza_cost()
if(dist!=0):
    obj2=DoorDelivery(size,quantity,topping,dist,obj1.cost)   
    print(obj2.pizza_cost())








 

        
           




























































