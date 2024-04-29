str1=""
str=input("enter a string")
for i in (str):
    if (i>="a" and i<="z"):
      i=chr(ord(i)-32)
      str1=str1+i
    elif (i>="A" and i<="Z"):
       i=chr(ord(i)+32)
       str1=str1+i
    else:
       str1=str1+i
print("output:{}".format(str1))