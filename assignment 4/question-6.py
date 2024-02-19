num=int(input('enter the number: '))
SUM=0
while (num<0):
    rem=num%10
    SUM=SUM+rem
    num=num//10
print('{}'.format(SUM))
