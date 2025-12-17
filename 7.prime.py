n=int(input("enter positive number="))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print(n,"is prime number")
else:
    print(n,"is not prime number")