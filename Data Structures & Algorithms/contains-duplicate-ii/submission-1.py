class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s=set()
        i=0
        for j in range(len(nums)):
            if nums[j] in s:
                return True
            s.add(nums[j])
            if j-i+1>k:
                s.remove(nums[i])
                i+=1
        return False

            
        