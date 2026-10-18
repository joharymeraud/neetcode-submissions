class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        s=0
        for i in range(len(prices)):
            if i==0:
                if prices[i+1]>prices[i]:
                    s-=prices[i]
            elif i ==len(prices)-1:
                if prices[i]>prices[i-1]:
                    s+=prices[i]
            elif prices[i-1]>= prices[i] and prices[i] < prices[i+1]:
                s-=prices[i]
            elif prices[i-1]< prices[i] and prices[i]>= prices[i+1]:
                s+=prices[i]
        return s 


        