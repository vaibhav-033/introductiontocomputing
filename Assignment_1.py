#1

a=int(input("Enter input 1:"))
b=int(input("Enter input 2:"))
c=int(input("Enter input 3:"))
(a+b+c)/3


#2

GI=int(input("Gross Income : "))        
NoD=int(input("No. of Dependents : "))
SD=10000
DD=3000
TI=GI-SD-(DD*NoD)
print(TI)
TR=0.2
Tax=TI*TR
print(Tax)


#3

time=int(input("No. of seconds : "))
minutes=time//60
print(minutes)
seconds=time%60
print(seconds)


#4

x=int(25)
y=int('25')
z=int(25.0)
x+y+z


#5

import math
a = 0
while a <= 345 :
    sin_a = math.sin(math.radians(a))
    cos_a = math.cos(math.radians(a))
    print(str(a) + " --- " + str(round(sin_a , 4)) + " " + str(round(cos_a , 4)))
    a += 15