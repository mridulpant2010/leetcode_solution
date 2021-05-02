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
            print(temp.val,sep='-',end='-')
            temp=temp.next

    def createLinkedlist(self,val):
        for el in val:
            if el!=-1:
                self.addElement(el)
                


def reverse_sub_list(head,p,q):
    
    if k<=1 or head is None:
        return head
    #if p==q:    return head
    curr,prev=head,None
    i=0
    while curr is not None and i<p-1:
        prev=curr
        curr=curr.next
        i+=1
    
    last_node_of_first_part=prev
    last_node_of_sub_list=curr
    
    i=0
    while curr is not None and i< q-p+1:
        next=curr.next 
        curr.next=prev 
        prev=curr
        curr = next 
        i+=1
        
    if last_node_of_first_part is not None:
        last_node_of_first_part.next=None 
    else:
        head=prev
    
    last_node_of_sub_list.next=curr
    #
    prev=last_node_of_sub_list
    return head


if __name__ == '__main__':
    n,k=list(map(int,input().split()))
    arr1=list(map(int,input().split()))
    l=LinkedList()
    l.createLinkedlist(arr1)
    #l.print_linkedlist()
    #l2.print_linkedlist()