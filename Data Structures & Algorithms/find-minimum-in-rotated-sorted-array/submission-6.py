class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo=0
        hi=len(nums)-1
        while lo<hi:
            g =(hi+lo)//2
            condition = nums[g]<=nums[len(nums)-1]
            if condition: hi=g
            else:lo=g+1
        return nums[lo]


        