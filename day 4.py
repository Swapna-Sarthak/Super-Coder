'''
import sys
def nearest_pal(n):
    for i in range(n+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
    
n=int(input(" "))
print(nearest_pal(n))
######################################################################
medical={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
l1=list(map(str,input().split(" ")))
spe=""
c=0
for i in medical.keys():
    if (l1.count(i)>c):
        c=l1.count(i)
        spe=i
print(medical[spe])
#####################################################################
'''
str1=input()
str2= input()
str3=""
for i in range (0,len(str1)):
    if(str1[i]!= " "):
        for j in range(0,len(str2)):
            if(str1[i] == str2[j]):
                str3+=str1[i]
                break
print(str3)          
#####################################################################
'''
class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
####################################################################
class Customer:
    def __init__(self,id):
        self.id = id #instead of id if i write 100 ,100 will be printed
        
c1=Customer(200)
print(c1.id)
######################################################################
class Book:

    def init(self):
        self.title=None

my_fav=Book()

my_fav.title="Head First Programming"
your_fav=Book () 
your_fav.title="Learn Python the hard way"

my_fav.title="Learning Python"

print("My favorite is", my_fav.title)
print("Your's is",your_fav.title)
#####################################################################
s1=input("")
print("ok",id(s1))
##################################################################
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material

    def __str__(self):
        return "Shoe with price: " + str(self.price) + " and material :" + self.material

a=int(input("enter price"))
b=input("enter material")
s1=Shoe(a,b) #Shoe(1000,"Canvas")
print(s1)
######################################################################
class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")
    def purchase(self):
        self.display()
        print("Calculating price")

Mobile().purchase()
m1=Mobile()
m2=Mobile()
m1=m2
print(m1)
print(m2)
#object is created but not initialized to any variable
###################################################################
class Mobile:
    def __init__(self, brand, price):
        self.price = price
        self.brand = brand
        self.total_price = None
    def purchase(self):
        if self.brand == "Apple":
            discount = 10
        else:
            discount = 5
        self.total_price = self.price - self.price * (discount /100)
        print("Total price of", self.brand, "mobile is", self.total_price)
    def return_money(self):
        if self.brand == "Apple":
            discount = 10
        else:
            discount = 5
        self.total_price = self.price * (discount /100)
        print("Return money", self.brand, "mobile is", self.total_price)
mob1=Mobile("Apple", 20000)
mob2=Mobile("Samsung", 10000) 
mob1.purchase()
mob2.purchase()
mob1.return_money()
mob2.return_money()
#########################################################################
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id= cust_id
        self.name= name
        self.age =age
        self.wallet_balance= wallet_balance
    def update_balance(self, amount):
        if amount < 1000:
            self.wallet_balance += amount
    def show_balance(self):
            print("The balance is ",self.wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance()
###################################################################
#WRONG
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id= cust_id
        self.name= name
        self.age =age
        self.__wallet_balance= wallet_balance
    def update_balance(self, amount):
        if amount < 5000:
            self.__wallet_balance += amount     #self.__wallet_balance =private self.wallet_balance =public
    def show_balance(self):
            print("The balance is ",self.__wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance()
print(c1.__wallet_balance())
#print(c1.self.__wallet_balance)
c1.update_balance(5000)
print(c1.show_balance())
#WRONG
'''
####################################################################
'''
class Dam:
    def __init__(self, name, length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam", 3.5)
print("Dam name:", dam1.name)
print("Dam Length", dam1.get_length())
####################################################################
class Table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self,glass_top, wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self, glass_top, wooden_top):
        self.assign_data(glass_top,wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate(True,True)
print(rate)
####################################################################
class Table:
    def __init__(self):
        print(id(self))
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
back_table=Table() 
front_table=back_table
back_table=dining_table
print(id(dining_table), id(back_table), id(front_table))
#print(dining_table, back_table,front_table)
'''



















































































































































