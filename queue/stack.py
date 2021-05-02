from collections import deque

class Stack:
    
    def __init__(self):
        self.q1=deque()
        self.q2=deque()
        self.top=None
        
    def push(self,val):
        self.q1.append(val)
    
    def pop(self):
        #make pop operation heavier
        if len(self.q1)==0:
            return 
        
        while len(self.q1)>1:
            self.q2.append(self.q1.popleft())
        
        self.top= self.q1[0]
        self.q,self.q1 = self.q1,self.q
        
        return self.top
    
    def empty(self):
        return len(self.q1)==0 and len(self.q2)==0
    
    def top(self):
        if len(self.q1)==0:
            return 
        while len(self.q1)>1:
            self.q2.append(self.q1.popleft())
        
        self.top= self.q1[0]
        self.q2.append(self.q1[0])
        self.q,self.q1 = self.q1,self.q
        
        

if __name__ == '__main__':
    pass