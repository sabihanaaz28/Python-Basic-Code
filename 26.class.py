class student:
    def  __init__(self):
        pass

    # def __init__(self,nm,rl):
    #     self.rollno=rl
    #     self.name=nm

    def getdata(self):
        self.rollno=int(input("enter roll number of student="))
        self.name=input("enter name of students =")

    def showdata(self):
        print("Roll No is=",self.rollno)
        print("Name is=",self.name)



arr=[]
n=int(input("how many records are insert in the list="))
for i in range(n):
    s=student()
    arr.append(s)

print(f"enter {n} records")
for i in range(n):
    arr[i].getdata()
print("all records are")
for i in range(n):
    arr[i].showdata()


def rollSearch(studRoll):
    j=0
    for i in arr:
        if i.rollno==studRoll:
            return j
        j+=1
    return-1


def nameSearch(studName):
    j=0
    for i in arr:
        if i.name==studName:
            return j
        j+=1
    return-1


while True:
    check=input("do you want to check the record y ? n=")
    if check=='n' or check=='N':
        print("thank you for using")
        break
    print("choices are=\n1.Roll no based \n2.Name based")
    choice=int(input("enter choices="))
    if choice==1:
        roll=int(input("enter roll number to be searched="))
        rollbase=rollSearch(roll)
        if rollbase==-1:
            print("data not found")
        else:
            arr[i].showdata()
        
    elif choice==2:
        name=input("enter name to be searched=")
        namebased=nameSearch(name)
        if namebased==-1:
            print("data not found")
        else:
            arr[i].showdata()
    else:
        print("please valid choice")