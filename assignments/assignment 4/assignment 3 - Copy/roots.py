a = float(input('Enter the coefficient a: '))
b = float(input('Enter the coefficient b: '))
c = float(input('Enter the coefficient c: '))
discriminant=b**2-4*a*c
if(discriminant>0) :
    print('quadratic equation has real roots')
elif(discriminant==0) :
    print('quadratic equation has real and equal roots')
else:
    print('quadratic equation has imaginary roots')
