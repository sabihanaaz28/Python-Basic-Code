def asc_order(array):
    length=len(array)
    for i in range(length):
        for j in range(length-i-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array
def dec_order(array):
    length=len(array)
    for i in range(length):
        for j in range(length-i-1):
            if array[j]<array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array
list1=int(input("how many number insert in the array="))
array=[]
for i in range(list1):
    num=int(input("enter any number="))
    array.append(num)
print("choices are=\n1.ascending order \n2.descending order")
choice=int(input("enter your choice="))
if choice==1:
    print("after ascending order with using bubble sort=",asc_order(array))

elif choice==2:
    print("after descending order with using bubble sort=",dec_order(array))

else:
    print("invalid choice")


   