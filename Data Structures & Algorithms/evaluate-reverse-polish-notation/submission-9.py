class Solution:
    def operation(self,n1,n2,op):
        if op =="+":
            return n1+n2
        if op=="-":
            return n1-n2
        if op=="*":
            return n1*n2
        if op=="/":
            return int(n1/n2)
    def evalRPN(self, tokens: List[str]) -> int:
        cur=0
        operations={"+","/","*","-"}
        pile=deque()
        for char in tokens:
            if char not in operations:
                pile.append(int(char))
            else:
                n2=pile.pop()
                n1=pile.pop()
                pile.append(self.operation(n1,n2,char))
        return pile[0]






        