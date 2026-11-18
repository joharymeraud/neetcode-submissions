class Solution:
    def mySqrt(self, x: int) -> int:
        lo=0
        hi=x
        while lo<hi:
            g = (lo+hi)//2+1
            if g*g==x:return g 
            elif g*g >x:hi=g-1
            else: lo=g
        return lo

        