class Solution:
    def twoSum(self,nums,k,start):
        r=[]
        i=start+1
        j=len(nums)-1
        while i<j:
            s = nums[i]+nums[j]
            if s==k:
                r.append([nums[i],nums[j]])
                i+=1
                j-=1
            elif s>k:
                j-=1
            else:
                i+=1
        return r
    
    def threeSum(self,nums,k,start):
        l=[]
        for idx in range(start+1,len(nums)):
            pairs = self.twoSum(nums,-nums[idx]+k,idx)
            if len(pairs)==0: continue
            for pair in pairs:
                newThree = [nums[idx]]+pair
                l.append(newThree)
        return l


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        r=[]
        nums.sort()
        d=set()
        for start in range(len(nums)):
            triplets = self.threeSum(nums,-nums[start]+target,start)
            if len(triplets)==0:continue
            for triplet in triplets:
                newFour = [nums[start]]+triplet
                t=tuple(newFour)
                if t not in d:
                    r.append(newFour)
                    d.add(t)
        return r







        