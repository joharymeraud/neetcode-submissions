class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        alr=set()
        maxi = 0 
        for num in nums: 
            if num-1 not in s and num not in alr:
                alr.add(num)
                k,i=0,0 
                while num+i in s:
                    k+=1
                    i+=1
                if k>= maxi:
                    maxi=k
        return maxi






                



        