class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = [0]*3
        for num in nums:
            l[num]+=1
        k=0
        for couleur in range(3):
            for _ in range(l[couleur]):
                nums[k]=couleur
                k+=1
            
        