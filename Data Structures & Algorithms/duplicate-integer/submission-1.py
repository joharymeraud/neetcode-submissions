class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums: 
            if i not in d:
                d[i] = 0
            else:
                return True
        return False