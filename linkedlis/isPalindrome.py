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

def reverse2(head):
    #print(head.value)
    if head.next is None or head is None:
        return head
    temp=reverse2(head.next)
    c=temp
    while c.next:
        c=c.next 
    c.next=head
    head.next=None
    return temp

def reverse3(head):
    #print(head.value)
    if head.next is None or head is None:
        return head
    head=reverse3(head.next)
    head.next.next=head
    head.next=None
    return head

def is_palindromic_linked_list(head):
    if head is None or head.next is None:
        return True
    slow=head
    fast=head
    a=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    
    head_second_half=reverse(slow)
    copy_head_second_half=head_second_half
    print(slow.value)
    while head is not None and head_second_half is not None:
        if head_second_half.value!=head.value:
            break
        head_second_half=head_second_half.next
        head=head.next
    reverse(copy_head_second_half)
    if head is None or head_second_half is None:
        return True
    return False
    

def printLinkedList(head):
    temp=head
    while temp:
        print(temp.value,end=' ')
        temp=temp.next
        
        

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  #head.next.next = Node(2)
  head.next.next.next = Node(2)
  head.next.next.next.next = Node(4)

  #print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  #head.next.next.next.next.next = Node(2)
  #print("Is palindrome: " + str(is_palindromic_linked_list(head)))
  
  #printLinkedList(head)
  
  #s=reverse(head)
  st=reverse3(head)
  #printLinkedList(s)
  #r=is_palindromic_linked_list(head)
  #print()
  #printLinkedList(s)
  print()
  printLinkedList(st)
main()



