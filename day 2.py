'''
#list
list1=[10,20,'alu',40.5]
print(list1)
list2=list([10,20])
print(list2)
list2.append(30)
print(list2)
list2.extend([40,50,60])
print(list2)
list2.insert(2,51)#index,value
print(list2)
list2.remove(51)
print(list2)
list2.pop(2)#empty means last value removed
print(list2)
del list2[1]
print(list2)
*********************************************************
def count_sen(s):
    n,l=0,0
    for i in s:
        if(i.isalpha()):
            l+=1
        elif(i.isdigit()):
            n+=1
        else:
            pass
    list1=[]
    list1.extend([n,l])
    return list1
a=input("Enter a sentence")
print("",count_sen(a))
#0rrrrrrrrrrrrrrrrrrrrrrrrrrrr
def count_sen(s):
    n,l=0,0
    for i in s:
        if(i.isalpha()):
            l+=1
        elif(i.isdigit()):
            n+=1
        else:
            pass
    list1=[]
    list1.extend([l,n])
    print(list1)
a=input("Enter a sentence")
count_sen(a)#ASCII
*********************************************************
def find_pairs(l1,sum1):
    b=0
    for i in range(0,len(l1)):
        for j in range(i+1,len(l1)):
            if(l1[i]+l1[j]==sum1):
                b+=1
                break
            else:
                continue
    if(b==0):
        return 0
    else:
        return b
l1=[int(i) for i in input().split()]
sum1=int(input())
print(find_pairs(l1,sum1))

**********************************************************
def str_sep(s1):
    if(len(s1)<2):
        return -1
    else:
        s2=""
        s2=s1[0:2]+s1[len(s1)-2:]
        return s2

s1=input("Enter a string")
print(str_sep(s1))
##########################################################
def str_sep(s1):
    s2="ing"
    if(len(s1)<3):
        return s1
    elif(s1[-3:]== s2):
        return s1+"ly"
    else:
        return s1+"ing"
s1=input("")
print(str_sep(s1))
########################################################
def check_duble(s1):
    s2=s1*2
    s1=str(s1)
    s2=str(s2)
    if(len(s1)==len(s2)):
        for i in s1:
            if(i in s2 and s1.index(i) != s2.index(i)):
               return True
            else:
                return False
    else:
        return False
s1=int(input())
print(check_duble(s1))
##########################################################
def find_avg(t1):
    t=0
    sum1=0
    for i in t1:
        sum1=sum1+i
        avg=sum1/10
    for i in t1:
        if (i>=avg):
            t+=1
    per=(t/10)*100
    return per
def gen_freq(t1):
    l1=[]
    for i in range(0,26):
        l1.append(t1.count(i))
    return l1

def sort_tuple(t1):
    t2=list(t1)
    t2.sort()
    return t2
    
t1=list(map(int,input().split(",")))
print(find_avg(t1))
print(gen_freq(t1))
print(sort_tuple(t1))'''
########################################################

#wpgoddict

########################################################
#list slicing

def sum_of_array(t1):
    t2=[]
    for i in range(1,len(t1)):
        for j in range(i,len(t1)):
            
            

n1=int(input(""))
n2=int(input(""))
result=[]
for i in range(n1,n2+1):
    result.append(i)
print(result)
array=[i for i in range(n1,n2+1)]
print(array)
result=[]




















































































































