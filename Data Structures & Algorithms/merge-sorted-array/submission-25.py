class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m=max(len(nums1)-len(nums2),0)
        n=len(nums2)
        j=len(nums2)-1
        i=m-1
        k=m+n-1
        while j >=0:
            if i>=0 and nums1[i]>=nums2[j]:
                nums1[k]=nums1[i]
                k-=1
                i-=1
            else:
                nums1[k]=nums2[j]
                k-=1
                j-=1





        
        

        