nm_marks=int(input("enter a nm marks="))
wd_marks=int(input("enter a wd marks="))
oop_marks=int(input("enter a oop marks="))
os_marks=int(input("enter a os marks="))
ds_marks=int(input("enter a ds marks="))
per=(nm_marks+wd_marks+oop_marks+os_marks+ds_marks)/5
print("percentage of student marks=",per)
if per>=90:
    print("grade A")
elif per>=80:
    print("grade B")
elif per>=70:
    print("grade C")
elif per>=60:
    print("grade D")
elif per>=50:
    print("grade E")
else:
    print("grade F")

