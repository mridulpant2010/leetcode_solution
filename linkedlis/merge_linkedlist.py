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

def mergeLinkedList(head1,head2):
    dummy=Node()
    root=dummy
    while head1 and head2:
        if head1.val<head2.val:
            dummy.next=head1
            dummy=dummy.next
            head1=head1.next
        else:
            dummy.next=head2
            head2=head2.next
            dummy=dummy.next
    
    while head1:
        dummy.next=head1
        head1=head1.next
        dummy=dummy.next
    while head2:
        dummy.next=head2
        head2=head2.next
        dummy=dummy.next
    return root.next

def printLinkedList(head):
    while head:
        print(head.val,sep=' ',end=' ')
        head=head.next

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
        h=mergeLinkedList(l.head,l2.head)
        printLinkedList(h)
        t-=1