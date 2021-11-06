# link of next node
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None



class Single_link:
    def __init__(self):
        # taking head node none
        self.head=None
    
    
    def print_traversal(self):
        # if head is null
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                # print each node single way
                print(n.data,"-->",end=" ")
                # changing the ref/link to  change the data/jump to next node 
                n=n.ref
    
    
    def add_beginning(self,data):
        # creating  new node in beginning
        beginNew_Node=Node(data)
        # transfering the previous head node ref to new node
        beginNew_Node.ref=self.head
        # changing the head of node
        self.head=beginNew_Node
    

    def add_ending(self,data):
        # creating new node at the end
        endNew_node=Node(data)
        if self.head is None:
            print("Single Linked list is empty\n")
            # if single link list is empty then endNew_node will be the head node
            self.head=endNew_node
        else:
            n=self.head
            # is list is not empty then we have to jump/pass from each node to the last node 
            while n.ref is not None:
                n=n.ref
            # assign the the previous last node ref from endNew_node
            n.ref=endNew_node
    
    
    def add_after(self,data,x):
        n=self.head
        # find the element in link list
        # if list is not none then while loop run
        while n is not None:
            # if x is equal to data given by user 
            if x==n.data:
                break
        
            n=n.ref
        # if list is empty
        if n is None:
            print("Item is not present in the single link list\n")
        else:
            # creating new node after the given element
            afterNew_node=Node(data)            
            # changing the refernce id with previous element
            afterNew_node.ref=n.ref
            n.ref=afterNew_node


    def add_before(self,data,x):
        n=self.head
        # if  node is not present
        if n is None:
            print("Item is not present in the single link list\n")
        # if list is empty
        if n.data==x:
            # creating the new node
            firstNew_node=Node(data)
            firstNew_node.ref=self.head
            self.head=firstNew_node
        
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref==None:
            print("node is not found")
        else:
            beforeNew_node=Node(data)
            # assigning the previous ref in new node
            beforeNew_node.ref=n.ref
             # assigning the new node ref to next node
            n.ref=beforeNew_node
        
    def add_empty(self,data):
        # if list is empty then only add the element
        if self.head is None:
            New_node=Node(data)
            self.head=New_node
        else:
            print("Linked list is not empty")

    
    def remove_first(self):
        # if no node is present
        if self.head is None:
            print("Linked list is empty")
        else:
            # change the head tag to the next node
            self.head=self.head.ref


    def remove_end(self):
        # if no node is present
        if self.head is None:
            print("Linked list is empty")
        else:
            # change the None tag to previous node
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None  


    def remove_by_value(self,x):
        if self.head is None:
            print("Linked list is empty can't remove node")
    
        if self.head.data == x:
            # change the head tag to the next node
            self.head=self.head.ref
        n=self.head
        # searching the give node
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not present")
        else:
            # assigning deleting node ref to previous node ref
            n.ref=n.ref.ref


SingleLinkList=Single_link()
SingleLinkList.add_beginning(10)
SingleLinkList.add_beginning(100)
SingleLinkList.print_traversal()










    