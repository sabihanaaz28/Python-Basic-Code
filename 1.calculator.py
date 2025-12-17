import math
while(True):
    print("****calculator****")
    a=int(input("enter first number="))
    b=int(input("enter second number="))
    print("choices are=\n1.addition \n2.subtraction \n3.multiplication \n4.modulus \n5.division \n6.floor \n7.power \n8.square root")
    choice=input("enter your choice=")
    if choice=='1':
        print("addition=",a+b)
    elif choice=='2':
        print("subtraction=",a-b)
    elif choice=='3':
        print("multiplication=",a*b)
    elif choice=='4':
        print("modulus=",a%b)
    elif choice=='5':
        print("division=",a/b)
    elif choice=='6':
        print("remainder=",a//b)
    elif choice=='7':
        print("power=",a**b)
    elif choice=='8':
        print("square root of a=",math.sqrt(a))
        print("square root of b=",math.sqrt(b))
    else:
        print("invalid choice")
    ans=input("do you want to continue y?n=")
    if ans=='n' or ans=='N':
        print("thank you for using my calculator")
        break