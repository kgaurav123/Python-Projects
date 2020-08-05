print(type("3"))
print(type('''3'''))
samp_string="This is a very important string"
print("Length is :",len(samp_string))
print(samp_string[0])
print(samp_string[-1])
print(samp_string[0:4])
print(samp_string[8:])
print(samp_string[0:-1:2])
print("Reverse is:",samp_string[::-1])
print("Green"+"Eggs")
print("Hello"*5)
num_string = str(4)
for char in samp_string:
  print(char)
for i in range(0,len(samp_string)-1,2):
  print(samp_string[i]+samp_string[i+1])

#uni code or ascii code
print("A =",ord("A"))
print("65 =",chr(65))

s=input("Enter string")
for i in range(0,len(s)):
  print(ord(s[i]),end=" ")
for char in s:
  print(ord(char))

#A_Z 65-90
#a-z 97-122
st=input("Enter the code")
norm_s=""
for char in st:
  norm_s+=str(ord(char)-23)
print(norm_s)
st=""
for i in range(0,len(norm_s)-1,2):
  char_code=norm_s[i]+norm_s[i+1]
  st+=chr(int(char_code)+23)
print(st)