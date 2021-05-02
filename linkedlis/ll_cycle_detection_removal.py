class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


# head - Head pointer of the Linked List
# Return a boolean value indicating the presence of cycle
# If the cycle is present, modify the linked list to remove the cycle as well
def floydCycleDetection(head):
    # Code here
    fastptr=head 
    slowptr=head 
    while fastptr is not None and fastptr.next is not None:
        fastptr=fastptr.next.next
        slowptr=slowptr.next 
        if slowptr==fastptr:
            return True 
    return False 

def floydCycleRemoval(head):
    if floydCycleDetection(head):
        pass 
    else:
        pass

# 
# 
# 
# 
# You do not need to refer or modify any code below this. 
# Only modify the above function definition.
# Any modications to code below could lead to a 'Wrong Answer' verdict despite above code being correct.
# You do not even need to read or know about the code below.
# 
# 
# 
# 


def buildCycleList():
    hash = {}
    inpArr = [int(x) for x in input().split()]
    x = inpArr[0]
    if x == -1:
        head = None
        return head

    head = Node(x)
    hash[x] = head
    current = head
    for x in inpArr[1:]:
        if x == -1:
            break
        if x in hash:
            current.next = hash[x]
            return head
        n = Node(x)
        current.next = n
        current = n
        hash[x] = n

    current.next = None
    return head


def printLinkedList(head):
    s = set()
    while head != None:
        if head.data in s:
            print("\nCycle detected at ", head.data, sep='', end='')
            return
        print(head.data, end=' ')
        s.add(head.data)
        head = head.next


head = buildCycleList()

cyclePresent = floydCycleRemoval(head)
if cyclePresent:
    print("Cycle was present")
else:
    print("No cycle")

print("Linked List - ", end='')
printLinkedList(head)
