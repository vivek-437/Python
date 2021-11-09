class Node:
    def __init__(self,data):
        # store data 
        self.data=data
        # store previous node link
        self.pref=None
        # store next node link
        self.nref=None

class doubleLinked_list:
    def __init__(self):
        # head node is None
        self.head=None
        

    def forward_traversal(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                # next ref
                n=n.nref


    def backward_traversal(self):
        print()
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            # find the last node
            while n.nref is not None:
                n=n.nref
            # backward printing the node
            while n is not None:
                print(n.data,"-->",end=" ")
                # previous ref
                n=n.pref
    

    def add_empty(self,data):
        new_node=Node(data)
        n=self.head
        if n is None:
            n=new_node
        else:
            print("Linked list is not empty")
    

    def add_beginning(self,data):
        new_node=Node(data)
        n=self.head
        if n is None:
            n=new_node
        else:
            new_node.nref=n
            n.pref=new_node
            n=new_node


    def add_end(self,data):
        new_node=Node(data)
        n=self.head
        if n is None:
            print("Likned list is empty")
            n=new_node
        else:
            while n.nref is not None:
                n=n.nref
            new_node.pref=n
            n.nref=new_node


    def add_after(self,data,x):
        new_node=Node(data)
        n=self.head
        if n is None:
            print("Linked list is empty")
            
        else:
            while n is not None:
                if x==n.data:
                    break
            n=n.nref
            if n is None:
                print("Given node is not present")
            else:
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node


    def add_before(self,data,x):
        new_node=Node(data)
        n=self.head
        if n is None:
            print("Linked list is empty")
            
        else:
            while n is not None:
                if x==n.data:
                    break
            n=n.nref
            if n is None:
                print("Given node is not present")
            else:
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    n=new_node
                n.pref=new_node
                

    def delete_begin(self):
        n=self.head
        if n is None:
            print("Linked list is empty")
        elif n.nref is None:
            n=None
            print("Linked list is empty after deleting the node")
        else:
            n=n.nref
            n.pref=None


    def delete_end(self):
        n=self.head
        if n is None:
            print("Linked list is empty")
        else:
            while n.nref is not None:
                if n.nref==None:
                    break
            n=n.nref
            if n.pref==None and n.nref==None:
                n=None
            else:
                n.pref.nref=None
                
    def delete_by_value(self,x):
        n=self.head
        if n is None:
            print("Linked list is empty")
        else:
            while n.nref is not None:
                if x==n.data:
                    break
            n=n.nref
            if n.pref is None and n.nref==None:
                n=None
            elif n.nref is None:
                n.pref.nref=None
            elif n.pref is None:
                n=n.nref
                n.pref=None
            else:
                n.pref=n.nref.pref
                n.nref=n.pref.nref


            

list=doubleLinked_list()
list.add_empty(10)
# list.add_end(20)
list.forward_traversal()
list.backward_traversal()