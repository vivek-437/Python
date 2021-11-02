numberOfElement=int(input("Enter the Size of Stack:- "))
stack1=[]
def push():
    if len(stack1)<numberOfElement:
        print("Enter the Number you wanna push:- ")
        a=int(input())
        stack1.append(a)
    elif len(stack1)>=numberOfElement:
        print("Stack is full")

def pop():
    print("Enter the Number you wanna push:- ")
    if len(stack1)==0:
        print("Stack is Empty\n")
    else:
        stack1.pop()
while True:
    print("1:-Enter 1 for push the element\n2:-Enter 2 for pop/remove the element\n3:-Enter 3 for exit\n4:-Display the stack element\n5:-Enter 5 to know the total elements in stack\n")
    Userinpt=int(input("Enter the Number:- "))
    if Userinpt==1:
        push()
    elif Userinpt==2:
        pop()
    elif Userinpt==3:
        break
    elif Userinpt==4:
        print(stack1)
    elif Userinpt==5:
        print(len(stack1))
    else:
        print("Enter correct number")
