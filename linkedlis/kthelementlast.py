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
    
    def kthfromLast(self,val):
        fast=self.head
        slow=self.head
        while val:
            fast=fast.next
            val-=1
        while fast:
            fast=fast.next
            slow=slow.next
        return slow.val
    
    def kthfromfirst(self,val):
        temp=self.head
        while val-1:
            temp=temp.next
            val-=1
        return temp.val
    
    def removeElements(self,val):
        curr=self.head
        prev=Node()
        next_p=self.head.next
        root=prev
        prev.next=curr
        while curr and curr.next:
            if curr.val==val:
                prev.next=next_p
                curr=next_p
                next_p=next_p.next
            else:
                next_p=next_p.next
                curr=curr.next
                prev=prev.next
        if curr.val ==val:
            prev.next=None
        return root.next
    
    def oddEvenList(self):
        slow=self.head
        fast=self.head.next
        prev=Node()
        root=prev
        prev.next=fast
        t=slow
        while fast and fast.next:
            slow.next=fast.next
            slow=slow.next
            prev=prev.next
            fast=fast.next.next
            prev.next=fast
        slow.next=root.next
        return t
    
    
    def getDecimalValue(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        temp2=self.head
        output=0
        while temp2 and count:
            an=temp2.val
            pw2=2**(count-1)
            output+=an*pw2
            count-=1
            temp2=temp2.next
        return output
    
    def kappend(self,l,k):
        temp1=self.head
        rem=l-k
        while temp1 and rem-1:
            temp1=temp1.next
            rem-=1
        next_p=temp1.next
        temp1.next=None
        temp2=next_p
        while temp2.next:
            temp2=temp2.next
        temp2.next=self.head
        return next_p
    
    def swapPairs(self):
        pass
            
        
    
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
    
def findCycleLength(slow):
    current=slow
    count=1
    current=current.next
    while current!=slow:
        current=current.next
        count+=1
    return count

    
def hasCycle(head):
    fast=head.next
    count=0
    slow=head
    prev=None
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            return findCycleLength(slow)
    # while fast!=slow :
    #     count+=1
    #     prev=fast
    #     fast=fast.next
    #     slow=slow.next
    # prev.next=None
    return False


def addTwoNumbers(head1,head2):
    temp1=head1
    temp2=head2
    h=None
    while temp1 and temp2:
        sum_v=temp1.val+temp2.val
        if sum_v<=9:
            h=Node(sum_v)
            
            
            
            
if __name__ == '__main__':
    # t=int(input())
    # while t:
    #     k=int(input())
    #     arr1=list(map(int,input().split()))
    #     m=int(input())
    #     arr2=list(map(int,input().split()))
    #     l=LinkedList()
    #     l.createLinkedlist(arr1)
    #     l2=LinkedList()
    #     l2.createLinkedlist(arr2)
    #     #l.print_linkedlist()
    #     #l2.print_linkedlist()
    #     h=mergeLinkedList(l.head,l2.head)
    #     printLinkedList(h)
    #     t-=1
    # s=int(input())
    # arr1=list(map(int,input().split()))
    # #k=int(input())
    # l=LinkedList()
    # l.createLinkedlist(arr1)
    # printLinkedList(l.oddEvenList())
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    #printLinkedList(head)
    print(hasCycle(head))
    