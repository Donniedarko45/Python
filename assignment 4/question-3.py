a=0
b=1
i=1
print('{} {}'.format(a,b))
while(i<20):
    fibn=a+b
    print('{}'.format(fibn),end=' ')
    i+=1
    a=b
    b=fibn
    
    
    
