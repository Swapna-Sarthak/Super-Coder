#Bounded method call and unbounded method call
'''
class OverDraw(Exception):
    pass
class LimitReached(Exception):
    pass
class Customer:
    def __init__(self,cid,cname,age,account):
        self.cid=cid
        self.cname=cname
        self.age=age
        self.account=account
    def withdraw(self,amount):
        try:
            if(amount>obj2.get_balance()):
                raise OverDraw
        except OverDraw:
            print("OverDraw")
            self.take_card()
            exit()
        obj2.set_balance(obj2.get_balance()-amount)
    def take_card(self):
        print("Take card out of the ATM")

    def get_customer_id(self):
        return self.cid
    def set_customer_id(self,new_id):
        self.cid=new_id
    def get_customer_name(self):
        return self.cname
    def set_customer_name(self,new_name):
        self.cname=new_name
    def get_age(self):
        return self.age
    def set_age(self,new_age):
        self.age=new_age
    def get_account(self):
        return self.account
    def set_age(self,new_account):
        self.account=new_account

class Acount:
    def __init__(self,account_type,balance,min_balance):
        self.__account_type=account_type
        self.__balance=balance
        self.__min_balance=min_balance
    def get_account_type(self):
        return self.__account_type
    def get_balance(self):
        return self.__balance
    def get_min_balance(self):
        return self.__min_balance
    def set_balance(self,new_balance):
        self.__balance=new_balance

class PrivilegedCustomer(Customer):
    def __init__(self,cid,cname,age,account,bonus_points):
        self.cid=cid
        self.cname=cname
        self.age=age
        self.account=account
        self.__bonus_points=bonus_points

    def withdraw(self,amount):
        super().withdraw(amount)
        self.__increase_bonus()
    def get_bonus_points(self):
        return self.__bonus_points
    def __increase_bonus(self):
        if(obj2.get_balance()>1000):
            self.__bonus_points+=10
        else:
            self.__bonus_points+=2

cid=int(input("Enter id"))
cname=input("Enter Name")
age=int(input("Enter Age"))
bonous_points=int(input("Enter Bonus Points"))
ctype=input("Enter account type")
balance=int(input("Enter account balance"))
obj1=PrivilegedCustomer(cid,cname,age,ctype,bonous_points)
obj2=Acount("Savings",balance,500)
amount1=int(input("Enter the value to be withdrawn"))
obj1.withdraw(amount1)
print("Customer balance:",obj2.get_balance())
print("Bonus points:",obj1.get_bonus_points())
try:
    if(obj2.get_balance()<obj2.get_min_balance()):
        raise LimitReached
except LimitReached:
    print("Limit Reached")
    obj1.take_card()
    exit()
obj1.take_card()
'''
############################################################################
def factor(num):
    sum1=1
    for i in range(2,num):
        if(num%i==0):
            sum1=sum1+i
    return sum1
l1=[int(x) for x in input(" ").split()]
#l1=[12,14]
l2=[]
c=0
for i in l1:
    if(factor(i) in l1):
        l2.append(i)
        c=1
if(c==0):
    print(-1)
else:
    print(*l2)
'''



















































