a=input("enter your string : ")
word=''
for i in a:
    if i != ' ':
        word+= i
    else:
        print(word)
        word=' '
print(word)