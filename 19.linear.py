n=int(input("how many numbers you want to have?"))
list1=[]
for i in range(n):
    x=int(input("enter any number="))
    list1.append(x)
item=int(input("enter number to be searche="))
for i in range(n):
    if item==list1[i]:
        print(f"{item} found at index {i}")
        break

else:
    print("item not found")