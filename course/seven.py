while True:
    try:
        number=int(input("Enter a number"))
        break
    except ValueError:
        print("You didn't entered any number")
    except:
        print("Unknown error occured")
 
print("Thanks for your response")


secret_number=7
while True:
    n=int(input("Enter a number"))
    if(n==secret_number):
        print("Bravo!you guessed it correct")
        break
    print("Sorry Guess again")

#from decimal import Decimal as D
from decimal import *

sum=Decimal(4)
sum+=Decimal("0.02")
sum+=Decimal("0.05")
sum-=Decimal("0.07")
print("sum={}".format(sum))

sum_1=Decimal(0)
sum_1+=Decimal("0.0111111111111111")
sum_1+=Decimal("0.0111111111111111")
print("sum=",sum_1)
sum_1-=Decimal("0.0222222222222222")
print("sum=",sum_1)
