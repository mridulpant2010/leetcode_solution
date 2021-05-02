class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
        
    def printList(self):
        temp=self
        while temp is not None:
            print(str(temp.value),end=' ')
            temp=temp.next
        print()
        
def reverse(head):
    prev=None
    curr=head
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev


def findmiddle(head):
    fastptr=head 
    slowptr=head
    while fastptr is not None and fastptr.next is not None:
        fastptr=fastptr.next.next
        slowptr=slowptr.next
    return slowptr


def reorder_elements(head):
    
    newNode=Node(-1)
    temp=newNode
    secondheader=findmiddle(head)
    secondNode=reverse(secondheader)
    print(secondNode.value,secondheader.value)
    secondNode.printList()
    head.printList()
    
    
    while secondNode is not None :
        newNode.next=secondNode
        secondNode=secondNode.next
        newNode=newNode.next
        newNode.next=head
        head=head.next
        newNode=newNode.next
    return temp
    

    
    
if __name__ == '__main__':
    head=Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    head.printList()
    a=reorder_elements(head)
    #a.printList()