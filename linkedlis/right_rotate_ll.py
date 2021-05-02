class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        
        
class LinkedList():
    def __init__(self):
        self.head=None
    
    def addElement(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            return 
        temp=self.head
        while temp.next :
            temp=temp.next
        temp.next=newNode
        
    def addHead(self,val):
        newNode=Node(val)
        newNode.next=self.head
        self.head=newNode
    
    def print_linkedlist(self):
        temp=self.head
        while temp:
            print(temp.val,sep=' ',end=' ')
            temp=temp.next

    def createLinkedlist(self,val):
        for el in val:
            if el!=-1:
                self.addElement(el)
                

    def right_reverse_linked_list(self,rotations):
        #
        temp =self.head
        ll_length=1
        while temp.next is not None:
            temp=temp.next 
            ll_length+=1
        
        temp.next=self.head
        rotations %= ll_length
        skip_length= ll_length-rotations
        
        last_node_first_part= self.head
        for _ in range(skip_length-1):
            last_node_first_part=last_node_first_part.next
            
        self.head= last_node_first_part.next 
        last_node_first_part.next=None 
             
    



if __name__ == '__main__':
    n = int(input())
    arr1=list(map(int,input().split()))
    t = int(input())
    l=LinkedList()
    l.createLinkedlist(arr1)
    #l.print_linkedlist()
    l.right_reverse_linked_list(t)
    l.print_linkedlist()
    #l2.print_linkedlist()