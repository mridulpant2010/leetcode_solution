class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(head):
    prev = None
    while (head is not None):
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev

def reverse_2(head,a,b):
    if head.next is None:
        return head
    if head is None:
        return head
    p=head
    q=head
    i=0
    temp=None
    while p is not None and i<a-1:
        temp=p
        p=p.next
        i+=1
    last_node_of_sub_list=p
    last_node_of_first_part=temp
    prev=None
    curr=p
    i=0
    while curr is not None and i<b-a+1:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
        i+=1
    if temp is not None:
        temp.next=prev
    else:
        head=prev
    last_node_of_sub_list.next=curr
    return head
        


def printLinkedList(head):
    temp=head
    while temp:
        print(temp.value,end=' ')
        temp=temp.next
        

if __name__=='__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    #head.next.next = Node(2)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    #head.next.next.next.next.next = Node(6)
    printLinkedList(head)
    st=reverse_2(head,2,4)
    printLinkedList(st)
    #r=is_palindromic_linked_list(head)
    #print()
    #printLinkedList(s)