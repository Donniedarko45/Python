a=0
b=1
i=1
num=int(input("enter a number to print the range of a fibnocii series: "))
print(a,b,end=' ')
while(num-1>=2):
    fibn=a+b
    print(fibn,end = " ")
    num-=1
    a=b
    b=fibn
print()
    
    
    
