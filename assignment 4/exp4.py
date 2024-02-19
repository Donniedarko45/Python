#1
fact=1
a=int(input("enter a number"))
for i in range(a,0,-1):
 fact=fact*i
print("factorial of {}={}".format(a,fact))
#2
sum1=0
a=int(input("enter a number"))
h=a
while (a>0):
 b=a%10
 sum1=sum1+(b**3)
 a=a//10

if sum1==h:
    print("the  number is armstrong")
else:
    print("the number is not armstrong")
#3
n=int(input("enter a number"))
n1=0
n2=1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()
#4
a=int(input("enter a number"))
flag=0
for i in range(2,a):
    if a%i==0:
        flag=1
    
if flag==0:
    print("the number is prime")
else:
    print("the number is not prime")
#5
sum1=0
a=int(input("enter a number"))
h=a
while (a>0):
 b=a%10
 sum1=(sum1*10)+b
 a=a//10

if sum1==h:
    print("the  number is palindrome")
else:
    print("the number is not palindrome")
#6
sum1=0
a=int(input("enter a number"))
while (a>0):
    rem=a%10
    sum1=sum1+rem
    a=a//10
print("sum={}".format(sum1))
#7
count=0
for i in range(1,101):
    if(i%5==0 and (i%7==0)):
        count+=1
        print(i,end=",")
print("\n")       
print("total numbers divisible by 5 and 7 between 1 and 100 are:",count)
#8
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
#9
lower =1
upper=100
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
#10
a=int(input("enter a number"))
for i in range(1,11):
    s=a*i
    print("{}*{}={}".format(a,i,s))
    

