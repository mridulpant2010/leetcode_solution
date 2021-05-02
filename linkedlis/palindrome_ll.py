#check if a ll is palindrome or not?
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList():
    def __init__(self):
        self.head=None
    
    def addElement(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            return 
        temp=self.head
        while temp.next is not None :
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
    
    def findMiddle(self):
        fast=self.head
        slow=self.head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next 
        return slow

    @staticmethod
    def reverse(head):
        prev=None
        curr=head 
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev = curr
            curr = next
        return prev


    def checkLinkedlist(self,middle):
        temp= middle.next
        first=self.head
        while temp is not None:
            if first.val!=temp.val:
                return False
            temp=temp.next
            first=first.next 
        return True

if __name__ == '__main__':
    n = int(input())
    arr1=list(map(int,input().split()))
    #t = int(input())
    l=LinkedList()
    l.createLinkedlist(arr1)
    #l.print_linkedlist()    
    middle=l.findMiddle()
    a=l.reverse(middle.next)
    #reversing the linkedlist
    middle.next=a
    if l.checkLinkedlist(middle) :
        print|('true')
    else:
        print('false')
    #correcting linkedlist
    b=l.reverse(middle.next)
    middle.next=b
    #l.print_linkedlist()