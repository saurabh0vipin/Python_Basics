num=int(input("enter a number: "))

res=1
if num<1:
    print("Enter a number greater than 0")
for i in range(1,num+1):
    res=res*i
print("factorial of",num, "is ", res)