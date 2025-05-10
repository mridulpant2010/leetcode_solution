from collections import defaultdict
class FreqStack:
    def __init__(self):
        # Write your code here
        self.max_freq = 0
        self.freq_stack = defaultdict(int)
        self.group = defaultdict(list)
        

    def push(self, value):
        # Write your code here
        self.freq_stack[value]+=1
        self.max_freq = self.freq_stack[value]
        self.group[self.max_freq].append(value)
        
    def pop(self):
        self.max_freq = max(self.group.keys())
        elem = self.group[self.max_freq].pop()
        self.freq_stack[elem]-=1
        print("popped element ",elem)
        if len(self.group[self.max_freq])==0:
            del self.group[self.max_freq]
        
        if self.freq_stack[elem]==0:
            del self.freq_stack[elem]
        return elem