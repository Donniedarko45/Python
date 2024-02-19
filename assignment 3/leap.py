year=int(input('enter the year to check whether it is leap year or not'))
if(year%4==0 and year%400!=0) :
         print('it is leap year')
elif(year%400==0) :
    print('it is leap year')
else:
    print('it is not a leap year')
         
