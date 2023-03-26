'''
#list comprehension version
result=[]
print([i for i in range(11) if i%2!=0])
print([i for i in range(11) if i%2==0])
print([i if i%2!=0 else i**2 for i in range (11)])
#list comprehension for matrix
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[mat[i][j]**2 if(mat[i][j]%2!=0) else mat[i][j]**3
        for i in range(len(mat))
                        for j in range(len(mat[0]))]
print(result)
#or i=row j=column
print([i**2 if i%2!=0 else i**3 for i in range (17)])
############################################################

mat=[[1,2,3],[4,5,6],[7,8,9]]
l2=[]
for i in range(0,len(mat)):
    l3=[]
    for j in range(0,len(mat[0])):
        if(mat[i][j]%2!=0):
            l3.append(mat[i][j]**2)
        else:
            l3.append(mat[i][j]**3)
    l2.append(l3)
print(l2)

#in list comprehension method
print([[mat[i][j]**2 if(mat[i][j]%2!=0) else mat[i][j]**3
        for i in range(0,len(mat))
        for j in range(0,len(mat[0]))]for i in range(0,len(mat))])
####################################################################
#list comprehension for matrix
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([[ele**2 if ele%2!=0 else ele**3
      for ele in row] for row in mat])
print([ele**2 if ele%2!=0 else ele**3
      for row in mat for ele in row])
###################################################################
mylist=[9,3,6,1,5,0,8,2,4,7]
listb=[6,4,6,1,2,2]
result=[]
for i in listb:
    for j in range(len(mylist)):
        if(i==mylist[j]):
            result.append((i,j))
print(result)
#or
mylist=[9,3,6,1,5,0,8,2,4,7]
listb=[6,4,6,1,2,2]
result=[]
for i in listb:
    result.append((i,mylist.index(i)))
print(result)
#or
print([(i,mylist.index(i))for i in listb])
###################################################################
sen=["a new world record was set",
     "in the holy city of ayodhya",
     "on the eve of diwali on tuesday",
     "with over three lakh diya or earthen lamps",
     "lit up simultaneously on the banks of the sarayu river"]
stop=['for','a','of','the','and','to','in','on','with','was']
result=[]     
for i in sen:
    l1=i.split(" ")
    l2=[]
    for j in l1:
        if(j not in stop):
            l2.append(j)
    result.append(" ".join(l2))
print(result)
#or

print([" ".join([j for j in i.split(" ") if(j not in stop)])
       for i in sen])
####################################################################
#sample
3,2,6,5,1,4,8,9
n1=3+2+6+9=20
n2=5148
op=5168

str1=list(map(int,input().split(",")))
s1=0
str2=""
for i in range (0,str1.index(5)):
    s1+=str1[i]
for i in range (str1.index(8)+1,len(str1)):
    s1+=str1[i]
for i in range(str1.index(5),str1.index(8)+1):
    str2+=str(str1[i])
print(s1+int(str2))
#OR
str1=list(map(int,input().split(",")))
s1=0
str2=""
for i in range (len(str1)):
    if(i < str1.index(5) or i > str1.index(8)):
        s1+=str1[i]
    else:
        str2+=str(str1[i])
print(s1+int(str2))
#OR

###################################################################
#rhdt:246
#if 2*2+4*4+6*6=56 is even so rotate rhdt=trhd
#elseif odd then rotate left by 2=>ghftd=ftdgh 1246
str1=input("").split(":")
s1=0
str2=""
for i in str1[1]:
    s1+=int(i)**2
if(s1%2==0):
    str2+=(str1[0][len(str1[0])-1]+str1[0][:len(str1[0])-1])
    print(str2)
else:
    str2+=str1[0][-3:-1]+str1[0][-1:]+str1[0][0:len(str1[0])-3]
print(str2)
#######################################################################
def large_prime(num,i):
    
    

n=int(input())
for i in range(n,n+9):
    sum+=p(i)
print(sum)
'''
def find_factors(num):
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    large=[]
    for i in list_of_factors:
        if is_prime(i,i//2)==True:
            large.append(i)
    return max(large)
    
def find_f(num):
    f=find_factors(num)
    l=find_largest_prime_factor(f)
    return l

def find_g(num):
    sum=0
    consicutive=[i for i in range(num,num+9)]
    for i in consicutive:
        largest_prime_factor=find_f(i)
        sum=sum+largest_prime_factor
    return sum

print(find_g(10))









































































































































































