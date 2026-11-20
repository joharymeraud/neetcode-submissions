class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rightpart=target<=nums[len(nums)-1]
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            g=(lo+hi)//2
            condition = (rightpart and nums[g] >= target and nums[g]<=nums[-1]) or ((not rightpart) and ((nums[g] >= target and nums[g]>nums[len(nums)-1]) or nums[g]<nums[len(nums)-1]))
            if nums[g]==target:return g
            elif condition: hi=g-1
            else:lo=g+1
        return -1
        