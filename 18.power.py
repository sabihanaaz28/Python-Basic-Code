def power(x,n):
    if n==0:
        return 1
    elif n<0:
        return 1/power(x,-n)
    else:
        return x * power(x,n-1)
x=int(input("enter a base element="))
n=int(input("enter an exponent element="))
print(f"{x} to the power {n}={power(x,n)}")

