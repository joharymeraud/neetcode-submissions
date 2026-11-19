class Solution:
    def tempsPris(self,piles,k):
        t=0
        for num in piles:
            coeff = num//k
            if num%k==0:t+=coeff
            else: t+=coeff+1
        return t

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini=1000000000
        maxi=max(piles)
        lo=1
        hi=maxi
        while lo<hi:
            g=(lo+hi)//2
            TP=self.tempsPris(piles,g)
            if TP==h and g<mini:
                mini=g
            elif TP>h:lo=g+1    
            else:hi=g
        return min(lo,mini)
        

        