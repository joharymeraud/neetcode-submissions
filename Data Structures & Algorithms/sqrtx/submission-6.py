class Solution:
    def mySqrt(self, x: int) -> int:
        lo=0
        hi=x
        while lo<hi:
            g = (lo+hi)//2+1
            if g**2==x:return g 
            elif g**2 >x:hi=g-1
            else: lo=g
        return lo

        