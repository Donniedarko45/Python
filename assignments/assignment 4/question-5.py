
a=int(input("enter a number to check whether it is pallindrome or not: "))
temp=a
sum=0
while (a>0):
 b=a%10
 sum=(sum*10)+b
 a=a//10

if sum==temp:
    print("{} is palindrome".format(sum))
else:
    print("{} is not palindrome".format(sum))
