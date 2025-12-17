stack=[]
def push(item):
    stack.append(item)

def pop():
    if len(stack)==0:
        print("stack is overflow")
    else:
        print("the pop element is=",stack.pop())
        

def peek():
    if len(stack)==0:
        print("stack is empty")
    else:
        print("the top element is=",stack[-1])


def display():
    print("display the all stack element\n",stack)


print("choices are =\n1.push \n2.pop\n3.peek \n4.display")
while True:
    choice=int(input("enter your choice="))
    match choice:
        case 1:
            item=int(input("enter push element="))

            push(item)          
        case 2:
            pop()

        case 3:
            peek()

        case 4:
            display()
            break

        case _:
            print("invalid choice")
        

