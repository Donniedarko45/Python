date=int(input('enter the date of the month: '))
month=int(input('enter the month of the year: '))
year=int(input('enter year: '))
if ((month==2 and (year%4==0 and year%100!=0) or (year%400==0) and date==29) or month==2 and date==28) or (month in [4,6,9,11] and date==30):
    date=1
    month += 1
elif(month==12 and date==31) :
    date=1
    month=1
    year+=1
elif(date<30 and month<=12):
    date+=1
else:
    print('entered date is not valid')
print('date is:',date)
print('month is {}'.format(month))
print('year is {}'.format(year))