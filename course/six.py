import random as r
n=r.randrange(1,51)
i=1
while i!=n:
    i+=1
print("{} is i and {} is random number".format(i,n))


i=1
while i<=20:
    if(i%2)==0:
        i+=1
        continue
    elif i==15:
        break
    print("odd {}".format(i))
    i+=1


n=int(input("How tall the tree should be:"))
spaces=n-1
hashes=1
stump_spaces=n-1
while n!=0:
    for i in range(spaces):
        print(" ",end="")
    for i in range(hashes):
        print("#",end="")
    print()
    n-=1
    spaces-=1
    hashes+=2
for i in range(stump_spaces):
    print(' ',end="")
print("#")
