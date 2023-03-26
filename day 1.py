'''
a=int(input("enter a"))
if (a%5==0 and a%3==0):
    print("Multiple of both 3 & 5")
elif(a%5==0):
    print("Mltiple of5")
elif(a%3==0):
    print("Multiple of 3")
else:
    print("Invalid")
***************************************************

for i in range(1,101):
    print(i,end=' ')
print()
for i in range(1,101,2):
    print(i,end=' ')
print()
for i in range(2,101,2):
    print(i,end=' ')
****************************************************

for i in range(100,0,-2):
    print(i,end=' ')
print()
for i in range(99,0,-2):
    print(i,end=' ')
****************************************************

for i in range(1,101):
    if(i==50):
        break
    print(i)
****************************************************


for i in range(1,101):
    if(i==50):
        continue
    print(i)

****************************************************

for i in range(1,101):
    if(i==50):
        pass
    #empty class or statement
    print(i,end=' ')
****************************************************
print()__str__

def function1(num1,num2):
    num3=num1+num2
    print("Addition=",num3)
function1(10,20)
#or 
def function1(num1,num2):
    num3=num1+num2
    return num3
print("haha",function1(10,20))
***************************************************

def function1(num1,num2):
    num3=num1+str(num2)
    return num3
print("haha",function1('10',20))
***************************************************
def function1(num1,num2):
    num3=num1+str(num2)
    return num3
print("haha",function1('10',20.5))
***************************************************

#positional arguments
def fun1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
fun1(10,100.5,'bhak',40)

#keyword arguments
def fun1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
fun1(num4=10,num1=100.5,num2='bhak',num3=40)
#default arguments
def fun2(name,rollno,branch,collegename="GIET"):
    print(name,rollno,branch,collegename)
fun2("alu",349,"CSE")
fun2("aluU",346,"CST")
fun2("aluuu",345,"BSE")
fun2("aluuuu",344,"ECE")
**************************************************
#variable number of arguments
def fun1(*alu):
    for i in alu:
        print(i,end=' ')
fun1(19,29)
print()
fun1(29,49,69,89)
print()
fun1(19,29,39,49,59,69)
#addition
def sum(*alu):
    sum1=0
    for i in alu:
        sum1=sum1+i
    return(sum1)
print(sum(19,29))
print(sum(29,49,69,89))
print(sum(19,29,39,49,59,69))
****************************************************
#PROBLEM
a=int(input())
b=int(input())
c=int(input())
if(a==7):
    print(b*c)
elif(b==7):
    print(c)
elif(c==7):
    print(-1)
else:
    print(a*b*c)
*****************************************************
#PROBLEM CURRENCY CALCULATOR
a=int(input("Enter amount of ruppes"))
name=input("Country name")
if(name=="Euro"):
    print(a*0.01417)
elif(name=="British Pound"):
    print(a*0.0100)
elif(name=="Austrelian dollar"):
    print(a*0.02140)
elif(name=="Canadian dollar"):
    print(a*0.02027)
else:
    print(-1)
    
******************************************************
#PROBLEM FLIGHT PRICE
a=int(input("Enter number of adults"))
b=int(input("Enter number of child"))
price=(a*37550 + b*12516.66)*(0.97)#+((a*37550 + b*12516.66)*(-0.03))#-((a*37550 + b*12516.66)*0.1)
#price+=(0.07*price) #WITH SERVICE TAX
#price-=(0.1*price) #AFTER HOLIDAY DISCOUNT
print(price)
******************************************************
'''
a=int(input("Enter number of 1"))
b=int(input("Enter number of 5"))
c=int(input("Enter total value"))
d=c/5
if(b>=d):
    print("Number of 5s=",int(d))
else:
    print(-1)
e=c%5
if(a>=e):
    print("Number of 1s=",int(e))
else:
    print(-1)






















