class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        if target >nums[high]:return high+1
        if target <nums[low]:return 0
        while low<high:
            mid = (high+low)//2
            if nums[mid]==target:return mid
            elif nums[mid]>target: high=mid
            else: low=mid+1
        return low

        