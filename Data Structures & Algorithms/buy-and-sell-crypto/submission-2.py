class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro=0
        minicourant=100
        procourant=0
        for j in range(len(prices)):
            if prices[j] <=minicourant:
                minicourant = prices[j]
            else:
                procourant=prices[j]-minicourant
            if procourant >=maxpro:
                maxpro=procourant
        return maxpro

            

        