M1=int(input('enter marks of COA: '))
M2=int(input('enter marks of Python: '))
M3=int(input('enter marks of Discrete mathematics: '))
M4=int(input('enter marks of Digital Electronics: '))
M5=int(input('enter marks of DSA: '))
percentage=(M1+M2+M3+M4+M5)/5
cgpa=percentage/10
if(M1<=100 and M2<=100 and M3<=100 and M4<=100 and M5<=100):
    if(cgpa>0 and cgpa<=3.4):
        print('you are fail')
    elif(cgpa>=3.5 and cgpa<=5.0):
         print('you got C+ grade')
    elif(cgpa>=5.1 and cgpa<=6.0):
        print('you got B grade')
    elif(cgpa>=6.1 and cgpa<=7.0):
        print('you got B+ grade')
    elif(cgpa>=7.1 and cgpa<=8.0):
         print('you got A grade')
    elif(cgpa>=8.1 and cgpa<=9.0):
        print('you got A+ grade')
    elif(cgpa>=8.1 and cgpa<=10.0):
        print('you got O grade')
    else:
     print('input marks in between 0 to 100')
    


