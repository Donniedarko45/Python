num=int(input('enter the number: '))
n=int(input('enter how many steps you want to shift: '))
print('right shift is: {}'.format(num/2**n))
print('left shift is: {}'.format(num*(2**n)))
