n=input("enter number=")
# n_str=str(n)
n_digit=len(n)
sum=0
for digit in n:
    sum+=(int(digit)**n_digit)
if sum==int(n):
    print(n,"is armstrong number")
else:
    print(n,"is not armstrong number") 

    