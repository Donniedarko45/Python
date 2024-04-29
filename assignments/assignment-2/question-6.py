a=float(input('enter the first side: '))
b=float(input('enter the second side: '))
c=float(input('enter the third side: '))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('area of triangle is: ',area)
