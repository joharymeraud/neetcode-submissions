class Solution:
    @staticmethod
    def sort(l1,l2):
        l=[]
        n1=len(l1)
        n2=len(l2)
        i,j=0,0
        while i <n1 and j<n2:
            if l1[i]<=l2[j]:
                l.append(l1[i])
                i+=1
            else:
                l.append(l2[j])
                j+=1
        return l +l1[i:]+l2[j:]


    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n==1:
            return nums
        else:
            l1=self.sortArray(nums[n//2:])
            l2=self.sortArray(nums[:n//2])
            return self.sort(l1,l2)

        