queue=[]
def enqueue(item):
    return queue.append(item)

def dequeue():
    if len(queue)==0:
        print("queue is underflow")
    else:
        print("the deletion element is=",queue.pop(0))

def peek():
    if len(queue)==0:
        print("queue is empty")
    else:
        print("the peek element is=",queue[0]) 
    
def display():
    print("display the all queue elements =\n",queue)



print("choices are=\n1.enqueue \n2.dequeue\n3.peek\n4.display")
while True:
    choice=int(input("enter your choice="))
    match choice:
        case 1:
            item=int(input("enter inqueue element="))
            enqueue(item)

        case 2:
            dequeue() 
        
        case 3:
            peek()
        case 4:
            display()
            break