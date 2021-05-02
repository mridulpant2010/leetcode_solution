#recursive code to reverse a linkedlist:

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
    
    
def merge(a,b):
    if a is None:
        return b
    if b is None:
        return a 
    
    c= Node()
    if a.val < b.val:
        c=a
        c.next=merge(a.next,b)
    else:
        c=b 
        c.next=merge(a,b.next)
    return c 

def printLinkedList(head):
    temp=head 
    while temp:
        print(temp.val,sep=' ',end=' ')
        temp=temp.next

if __name__ == '__main__':
    t=int(input())
    while t:
        k=int(input())
        arr1=list(map(int,input().split()))
        m=int(input())
        arr2=list(map(int,input().split()))
        l=LinkedList()
        l.createLinkedlist(arr1)
        l2=LinkedList()
        l2.createLinkedlist(arr2)
        #l.print_linkedlist()
        #l2.print_linkedlist()
        h=merge(l.head,l2.head)
        printLinkedList(h)
        t-=1


