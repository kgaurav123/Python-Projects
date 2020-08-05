'''# for and range
for i in [2,4,6,8,10]:
    print("i =",i)
for i in range(10):    # 0 - 9
    print("i =",i)
for i in range(2,5):  # 2,3,4
    print("i =",i)
n=7
print("is {} even {}".format(n,(n%2==0)))
for i in range(1,21):
    if(i%2==0):
        print("{} is even".format(i))
    else:
        print("{} is odd".format(i))
b=float(input("Enter a decimal "))
print("Rounded to two decimals:{:.2f}".format(b))'''
r=float(input("Enter rate of interest"))
p=float(input("Enter principal to be invested"))
for i in range(10):
    p=p+p*r/100
print("Money invested after 10 years is {:.2f}".format(p))
print("2+3*4",2+3*4)
print("2+(3*4)",2+(3*4))
print("(2+3)*4",(2+3)*4)
