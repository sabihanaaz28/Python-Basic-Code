def countdown(n):
    if n>=1:
        print(n,end=" ")
        n-=1
        countdown(n)
n=int(input("enter a number="))
countdown(n)