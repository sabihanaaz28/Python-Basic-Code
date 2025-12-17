n=int(input("how many numbers you want to have?"))
l1=[]
for i in range(n):
    x=int(input("enter any element="))
    l1.append(x)
item=int(input("enter number to be searched=  "))
beg=0
end=n-1
while beg<=end:
    mid=(beg+end)//2
    if l1[mid]==item:
        print(f"{item} found at index {mid}")
        break
    elif l1[mid]<item:
        beg=mid+1
    else:
        end=mid-1
else:
    print(f"{item} is not found")
