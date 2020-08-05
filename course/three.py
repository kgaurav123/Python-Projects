#miles to kilometers
n=int(input())
p=n*1.60934
print("{}".format(p))
#Math functions
import math as m
print("ceil(4.4)={}".format(m.ceil(4.4)))
print("floor(4.4)={}".format(m.floor(4.4)))
print("fabs(-4.4)={}".format(m.fabs(-4.4)))
print("factorial(4)={}".format(m.factorial(4)))
print("fmod(7,4)={}".format(m.fmod(7,4))) #remainder of division(7%4)
print("pow(3,4)={}".format(m.pow(3,4)))
print("sqrt(4)={}".format(m.sqrt(4)))
print("truncate(4.7)={}".format(m.trunc(4.7)))#recieve a float and return to int
#special values
print("pi={}".format(m.pi))
print("e={}".format(m.e))
print("log(e^2,e)={}".format(m.log(pow(m.e,2),m.e)))
print("log10(100)={}".format(m.log10(100)))
#trigonometric functions
print("sin(pi/2)={}".format(m.sin(m.pi/2)))
print("sinh(1)={}".format(m.sinh(1)))
print("acos(-1)={}".format(m.acos(-1)))  #outpur in radians
print("degrees(1.57)={}".format(m.degrees(1.57)))
print("radians(180)={}".format(m.radians(180)))
