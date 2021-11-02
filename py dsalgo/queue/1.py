queue_Size=int(input("Enter the size of Queue:- "))
queue=[]


def Enqueue():
    if len(queue)<queue_Size:
        enqueue_Element=input("Enter the Element you wannna store in queue:- ")
        queue.append(enqueue_Element)
    elif len(queue)>=queue_Size:
        print("Queue is full\n")


def Dequeue():
    if len(queue)==0:
        print("Queue is Empty\n")
    else:
        queue.pop(0)


while True:
    print("1:-Enter 1 to store a element in Queue\n2:-Enter 2 to delete the element\n3:-Enter 3 to check the size of Queue occupied\n4:-Enter 4 to exit\n5:-Enter 5 to display the Queue")
    useript=int(input("Enter the Number:- "))
    if useript==1:
        Enqueue()
    elif useript==2:
        Dequeue()
    elif useript==3:
        print(f"Total number of element in Queue {len(queue)}")
    elif useript==4:
        print(queue)
        break
    elif useript==5:
        print(queue)
    else:
        print("Enter the valid Number")