class Solution:
    def tempsArrive(self,position,speed,target):
        return (target-position)/speed
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed), reverse=True)
        c=1
        pile=deque()
        for p,v in cars:
            if not pile: pile.append((p,v,self.tempsArrive(p,v,target)))
            elif self.tempsArrive(p,v,target)>self.tempsArrive(pile[-1][0],pile[-1][1],target):
                c+=1
                pile.append((p,v,self.tempsArrive(p,v,target)))
        return c








        