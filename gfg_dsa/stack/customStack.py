class CustomStack:
    
    def __init__(self, maxSize: int):
        self.size=maxSize
        self.arr=[]
        self.sz=0

    def push(self, x: int) -> None:
        if len(self.arr)<self.size:
            self.arr.append(x)
            self.sz+=1
            return
            
    def pop(self) -> int:
        if len(self.arr)==0:
            self.sz=0
            return -1
        else:
            top=self.arr[-1]
            self.arr.pop()
            self.sz-=1
            return top

    def increment(self, k: int, val: int) -> None:
        if len(self.arr)==0:
            return 
        else:
            for i in range(min(self.sz,k)):
                self.arr[i]=self.arr[i]+val
    
    def print_st(self):
        return self.arr

# ["CustomStack","push","pop","increment","pop","increment","push","pop","push","increment","increment","increment"]
# [[2],[34],[],[8,100],[],[9,91],[63],[],[84],[10,93],[6,45],[10,4]]
obj = CustomStack(2)
obj.push(34)
obj.pop()
obj.increment(8,100)
obj.pop()
obj.increment(9,91)
obj.push(63)
obj.pop()
obj.push(84)
print(obj.print_st())
obj.increment(10,93)
obj.increment(6,45)
obj.increment(10,4)
print(obj.print_st())



# obj = CustomStack(0)
# obj.push(1)
# print(obj.pop())
# # obj.pop()
# # obj.pop()
# # obj.pop()
# # obj.pop()
# print(obj.print_st())



