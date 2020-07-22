import string 
import random
def gen():
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    s=[]
    paslen=int(input("Enter the length of password to be generated"))
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    pas=("".join(s[0:paslen]))
    print(pas)
gen()