p=input("enter your password: ")
count_up=0
count_low=0
count_spcl=0
count_num=0
for i in p:
    if(i>='A' and i<='Z'):
        count_up+=1
    if(i>='a' and i<='z'):    
        count_low+=1            
    if(i>='0' and i<='9'):  
        count_num+=1  
    else: 
        count_spcl+=1

if(count_up<2 or count_low<2 or count_spcl<2 or count_num<2):
    print("invalid password entered")
elif len(p)<=8:
    print("weak pass")
elif len(p)>8 and len(p)<=10:
    print("medium pass")    
elif len(p)>10:
    print("strong pass")
