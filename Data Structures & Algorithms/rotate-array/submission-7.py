class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        compteur=0
        idx,i=0,0
        while compteur<n:
            start,old=idx,nums[idx]
            while start != (idx+k)%n:
                old,nums[(idx+k)%n]=nums[(idx+k)%n],old
                compteur+=1
                idx=(idx+k)%n
            old,nums[(idx+k)%n]=nums[(idx+k)%n],old
            compteur +=1
            idx=(idx+k)%n    
            i+=1
            idx=i
        
                       
            



