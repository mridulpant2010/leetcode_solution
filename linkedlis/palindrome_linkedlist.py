class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    #@staticmethod
    def printNode(self):
        temp=self
        while temp is not None:
            print(temp.value,end=' ')
            temp=temp.next
        print()
    
def findMiddle(head):
    fast=head
    slow=head
    while fast is not None and fast.next is not None:
        fast=fast.next.next
        slow=slow.next 
    return slow

def reverse(head):
    prev=None
    curr=head 
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev = curr
        curr = next
    return prev


def checkLinkedlist(middle,head):
    temp= middle.next
    first=head
    while temp is not None:
        if first.value!=temp.value:
            return False
        temp=temp.next
        first=first.next 
    return True
        
        
if __name__ == '__main__':
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    
    #print("Is palindrome: " + str(is_palindromic_linked_list(head)))
    #middle=findMiddle(head)
    #print(middle.value)
    #head.next.next.next.next.next = Node(2)
    #print("Is palindrome: " + str(is_palindromic_linked_list(head)))
    
    head.printNode()
    middle=findMiddle(head)
    print(middle.value)
    
    #reversing the linkedlist
    a=reverse(middle.next)
    a.printNode()
    middle.next=a
    print('after converting the linkedlist')
    head.printNode()
    
    print(checkLinkedlist(middle,head))
    
    #correcting linkedlist
    b=reverse(middle.next)
    middle.next=b
    print(head.printNode())