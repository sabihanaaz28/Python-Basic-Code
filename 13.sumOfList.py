list1=[90,20,80,79,60,70,50,99]
greater=list1[0]
smaller=list1[0]
sum=0
for i in list1:
    sum+=i
    if greater<i:
        greater=i
    if smaller>i:
        smaller=i
print("greater number is=",greater)
print("smaller number is=",smaller)
print("sum of list=",sum)