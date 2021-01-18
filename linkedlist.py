

class Node:
    
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=None
    
    def get(self,index):
        count=1
        temp=self.head
        while temp:
            pass
    
    def addAtHead(self,val):
        temp = Node(val)
        temp.next=self.head
        self.head=temp
    
    
    def addAtTail(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            return
        temp=self.head
        while temp.next is None:
            temp=temp.next
        temp.next=newNode
    
    def addAtIndex(self,index,val):
        count=1
        temp=self.head
        newNode = Node(val)
        #if the index is 0
        if index==0:
            self.addAtHead(val)
        
        while temp.next:
            if index==count:
                newNode.next=temp.next
                temp.next=newNode
                return 
            else:
                temp=temp.next
                count+=1
        
        
        
        
        #if the index is at last
    
    def deleteBeginning(self):
        self.head=self.head.next
    
    def deleteAtIndex(self,index):
        count=1
        if index==0:
            self.deleteBeginning()
        temp=self.head
        while temp.next:
            if count==index-1:
                next_e=temp.next
                temp.next=next_e.next
                return
            else:
                temp=temp.next
                count+=1
        
    