num=int(input("How many terms do you want: "))

count=1
a=0
b=1
if num<0:
    print("Nothing to print")
else:
    while count<num:
        if count == 1:
            print(a)
        elif count == 2:
            print(b)
        else:
            print(a+b)
            temp=a+b
            a=b
            b=temp
        count=count+1


