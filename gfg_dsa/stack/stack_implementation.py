'''
application of stack
1- function calls
2- checking for balanced paranthesis
3- reversing items
4- infix to prefix/postfix
5- evaluation to prefix/postfix
6- stock span problem and its variations
7- forward/backward


implementation of stack in python
1- using list :
    --append at the end 
    --remove at the end
2- using collections.deque : it is the implementation of a doubley-linked list
    --
3- using queue.LIFO_queue -- not required to study more as it is mainly used in a multi-threaded env
4- using our own implementation
'''

'''
using list
'''


'''
using deque
it is an implementation of the doubley linked list.
'''
from collections import deque
stack = deque()
#append operation
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)
stack.pop()

import math
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class MyStack:
    def __init__(self):
        self.head = None
        self.sz = 0

    def push(self, x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.sz = self.sz+1

    def size(self):
        return self.sz

    def peek(self):
        if self.head == None:
            return math.inf
        return self.head.data
    def pop(self):
        if self.head==None:
            return math.inf
        res=self.head.data
        self.head=self.head.next
        self.sz=self.sz-1
        return res


s=MyStack()
s.push(10)
s.push(20)
s.push(30)
s.push(60)
print(s.pop())
print(s.peek())
print(s.size())
print(s.peek())



