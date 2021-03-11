#Node class
class Node:

    #Function to initialize the node object
    def __init__(self,data):
        self.data = data #assign data
        self.next = None #initialize next as null

#Linked List Class
class LinkedList:
    #Function to initialize the Linked List object
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        #1 & 2: Allocate the node & put in the data
        new_node = Node(new_data)
        #3: Make next of new node as head
        new_node.next = self.head
        #4: Move the head to poitn new node
        self.head = new_node

    def insertAfter(self,prev_node,new_data):
        #1: check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must in be in LinkedList.")
            return
        #2: create new node and put in the data
        new_node = Node(new_data)
        #3: make next of new node as next of prev_node
        new_node.next = prev_node.next
        #4: make next of prev_node as new node
        prev_node.next = new_node
    
    def append(self,new_data):
        #1: create a new node
        #2: put in the data
        #3: sset next as none
        new_node = Node(new_data)

        #4: if the LinkedList is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return
        
        #5: else traverse till the last node
        last = self.head
        while(last.next):
            last = last.next
        
        #6. change the next of last node
        last.next = new_node

    def deleteNode(self,key):
        #store head node
        temp=self.head
        #if head node itself holds the key to be dleted
        if(temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp=None
                return
            
        #search for the key to be dleted, keep track of the previos node as we need to chance 'prev.next'
        while(temp is not None):
            if temp.data==key:
                break
            prev=temp
            temp=temp.next

        #if key was not present in linked list
        if(temp==None):
            return
            
        #unlink the node from the linked list
        prev.next = temp.next

        temp = None

            

#Code execution starts here
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion of 1")
llist.printList()