start=int(input("enter start number="))
end_num=int(input("enter end number="))
while True:
  if(start<1):
    start=int(input('Enter start number  '))
  elif(start>end_num):
    endNum=int(input('Enter end number '))
  else:
    break
for i in range (start,end_num+1):
  rev=i
  num=0
  count=0
  while (rev>0):
    count+=1
    rev//=10
  rev=i
  while(rev>0):
    temp=rev%10
    num=num*10+temp
    rev//=10 
  if(num==i):
    print(i ,end=' ')  
  
  
