class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=[]
        self.elements=0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.elements+=1
        if len(self.mini)==0:self.mini.append(val)
        else:
            if val <self.mini[-1]:self.mini.append(val)
            else: self.mini.append(self.mini[-1])

    def pop(self) -> None:
        self.elements-=1
        self.mini.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.elements==0:return None
        return self.mini[self.elements-1]

        
