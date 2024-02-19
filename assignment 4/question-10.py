# printing table
num=int(input('enter a number to print the table: '))
for i in range(1,11):
    table=num*i
    print('{}*{}={}'.format(num,i,table))
