a = float(input('Enter the coefficient a: '))
b = float(input('Enter the coefficient b: '))
c = float(input('Enter the coefficient c: '))
discriminant=b**2-4*a*c
if(discriminant>0) :
    root1= (-b+(discriminant**0.5))/2*a
    root2= (-b-(discriminant**0.5))/2*a
    print('quadratic equation has real roots:{} {} '.format(root1,root2))
elif(discriminant==0) :
    root=-b/2*a
    print('quadratic equation has real and equal roots: {} {]'.format(root,root))
else:
    root1= (-b+(discriminant**0.5))/2*a
    root2= (-b-(discriminant**0.5))/2*a
    print('quadratic equation has imaginary roots {} {}'.format(root1,root2))
