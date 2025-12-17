import math
startNum=int(input("Enter start number="))
endNum=int(input("Enter end number ="))
while True:
  if(startNum<1):
    startNum=int(input("Enter start number ="))
  elif(startNum>endNum):
    endNum=int(input("Enter end number="))
  else:
    break

for i in range (startNum,endNum+1):
  numCopy=i
  newNum=0
  count=0
  # count number of digits in number
  while (numCopy>0):
    count+=1
    numCopy//=10
  
  # creating reverse of number
  numCopy=i
  while(numCopy>0):
    temp=numCopy%10
    sqr=math.pow(temp,count)
    newNum=newNum+sqr
    numCopy//=10
    
  # checking both are same or not
  if(newNum==i):
    print(i ,end=' ')  
  
  