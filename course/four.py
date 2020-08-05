#Conditional Operators
drink=input("Pick one(coke or pepsi):")
if drink=="coke":
    print("Here is your coke")
elif drink=="pepsi":
    print("Here is your pepsi")
else:
    print("Here is your water")

def arith():
    n1,operator,n2=input("Enter n1,operator,n2").split()
    n1=int(n1)
    n2=int(n2)
    if operator=="+":
        print("{}+{}={}".format(n1,n2,n1+n2))
    elif operator=="-":
        print("{}-{}={}".format(n1,n2,n1-n2))
    elif operator=="*":
        print("{}*{}={}".format(n1,n2,n1*n2))
    elif operator=="/":
        print("{}/{}={}".format(n1,n2,n1/n2))
    else:
        print("Use only +,_,* or / ")
        arith()
arith()
age=int(input("Enter age:"))
if (age>=1) and (age<=18):
    print("Important birthday")
elif not age<65:
    print("old birthday")
else:
    print("Not important birthday")
#ternary operator
age=int(input("Enter your age"))
can_vote=True if age>18 else False
print("you can vote {}".format(can_vote))