
import heapq

class MaxStack:

    def __init__(self):
       # Write your code here
        self.stack=[]
        self.he=[]
        self.popped=set()
        self.num_id=0

    def push(self, x):
        # Write your code here
        #self.he.append(x)
        self.stack.append((x,self.num_id))
        heapq.heappush(self.he,(x,self.num_id))
        self.num_id+=1

    def pop(self):
        # Write your code rhere
        if self.popped:
            pop_idx=next(iter(self.popped))
            
        while self.stack and 
            return self.stack.pop()

    def top(self):
        # Write your code here
        

    def peekMax(self):
        # Write your code here
        max_element=heapq.heappop(self.he)
        # but how are you going to remove it from the stack now

    def popMax(self):
        # Write your code here
        pass