class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=100001
        s=0
        start=0
        for i, num in enumerate(nums):
            s+=num
            while s >=target:
                if i-start+1<mini:mini=i-start+1
                s-=nums[start] 
                start+=1
        if mini ==100001:return 0
        return mini

