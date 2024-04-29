temp=input("enter a string: ")
count=0
for i in temp:
    if (i in ('aeiouAEIOU')):
        count+=1
print('total number of vowels in a string is: {}'.format(count))        
        
    
