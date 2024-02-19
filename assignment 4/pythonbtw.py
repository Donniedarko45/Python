count=0
n=2
for i in range(2,101):
    if n%i==0:
        n+=1
        count+=1
print('{}'.format(count))        
        
