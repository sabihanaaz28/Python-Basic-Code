def asc_order(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]>array[j]:
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
    return array



def dec_order(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]<array[j]:
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
    return array


list1=int(input("how many number insert in the array="))
array=[]
for i in range(list1):
    num=int(input("enter any number="))
    array.append(num)
print("choices are=\n1.ascending order \n2.descending order")
choice=int(input("enter your choice="))
if choice==1:
    print("after ascending order with using selection sort=",asc_order(array))

elif choice==2:
    print("after descending order with using selection sort=",dec_order(array))

else:
    print("invalid choice")


 