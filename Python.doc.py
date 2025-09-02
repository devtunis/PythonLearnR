#delc var 


#a_ =19
#a$ = 3
#3a=4
#a3 =4
a = 10
a = 43
a  = 0

r  = 10

#operation betw var

# mod(%)  div(//)  add(+)  minus(-) pow(*)

print(4%2)  =  #be9i
print(4//2)  = # 2.333  = 2
print(4+2)  = # 6  
print(4-2)  = # 2  
print(4*2)  = #8
print(4**2)  = #16

#type of var

# int  4343434
#bool  0/1  True /False
# str    "dzdadadad"
#object    {key:value}
#array     [1,2,5]
#float 1.32323
 


#opration betw str

a = "abcd"
b = "fgeie"
print(a+b)
#built in function 
a = 2
b = "hello"
print(str(a)+b)

#add
a = 2
b = "2"
 
print("somme de 2 var est =  ",a+int(b))  
#swap exmple 

# declare 2 var  swap
# pow
x  = 1
y  = 3
 
aux  = x
x  =y
y =   aux
#exmple x,y = y,x

print("after",x,y)

#inputs

a =int(input("ENTER YOUR NUMBER ="))
b =int(input("ENTER YOUR NUMBER ="))
print("sum=",a+b)
# condtion ()
#and or 
age = int(input("taper votre age"))
couple = input("you have couple  yes or no")
sal  = float(input("taper votre salaire"))
lang__speak = int(input("how lang do u speak"))
if((age >=18 and couple=="yes"and age <=60) and ( sal > 1000 ) and lang__speak >= 10 ):
    print("welcome")
else:
    print("you under -18 bara raw7")

#exerice

from math import*
from random import*

x=3
y=10
TYPE__OPERATION  ="sqrt"
 

if(TYPE__OPERATION!="+" or  TYPE__OPERATION !="-" or TYPE__OPERATION!="random" or TYPE__OPERATION!="sqrt" or TYPE__OPERATION!="**" or TYPE__OPERATION!="*" or TYPE__OPERATION!="//"  or TYPE__OPERATION !="%"):
    if(TYPE__OPERATION=="+"):
        print("sum",x+y)  
    elif TYPE__OPERATION=="-":
        print("minus",x-y) 

    elif TYPE__OPERATION=="*":
        print("mul",x*y)
    elif TYPE__OPERATION=="**":
        print("power of x and y ",x**y)

    elif TYPE__OPERATION=="//":
        print("div",x//y) 
    elif TYPE__OPERATION=="random":
        print("random",randint(x,y))  

    elif TYPE__OPERATION=="sqrt":
        print("sqrt",sqrt(x))
    elif TYPE__OPERATION=="%":
        print("mode",x%y)
  
        
else:
    print("operation invalid try do +   - * ")
    print("error 404 ?")

# test about (sous chaine ) methode (len,users[index])
user  = "nahdigyth@gmail.com"
 
if user[0] == "n" and user[len(user)-1]=="m" and user[(len(user)-1)//2]=="@" :
    print("200")
else:
    print("404")

# find methode

user  = "nahdigyth@gmail.com"
if  user.find("@")!= -1:
    print("welcome")
else:
    print("404")

#know domain to each user
user1 = "nahdigyth@gmail.com"
start = user1.find("@")+1
end   = len(user1)
print(user1[start:end ])

#array , list 

t = [1,2,3,4,5]
print(t[0])

#exmple list 

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a[3][0])

# pretty exmple 

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a[3][0]+" "+a[0]+" "+a[1])

#remove value from list

fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)
