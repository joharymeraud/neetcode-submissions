class Solution:
    def mySqrt(self, x: int) -> int:
        lo=0
        hi=x
        while lo<hi:
            g = (lo+hi)//2
            if g**2==x:return g 
            elif g**2 >x:hi=g
            else: lo=g+1
        if lo**2==x:return lo
        else: return max(0,lo-1)
        