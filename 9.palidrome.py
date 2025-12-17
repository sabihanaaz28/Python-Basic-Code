n=int(input("enter any number="))
rev=0
temp=n
while(temp!=0):
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
if n==rev:
    print(n,"is palidrome")
else:
    print(n,"is not palidrome")
