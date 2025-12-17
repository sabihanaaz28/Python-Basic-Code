start=int(input("enter start number="))
end_num=int(input("enter end number="))
count=0
while True:
    if start<1 :
        start=int(input("enter start number="))
    elif start>end_num:
        end_num=int(input("enter end number="))
    else:
        break
for i in range(start,end_num+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        print(i,end=" ")
print("\n it is all the prime number")

