class Solution:
    def twoSum(self,nums,k):
        r=[]
        i=0
        j=len(nums)-1
        while i <j:
            summ=nums[i]+nums[j]
            if summ==k:
                r.append([nums[i],nums[j]])
                j-=1
                i+=1
            if summ>k:
                j-=1
            if summ<k:
                i+=1
        return r
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        d=set()
        l=[]
        for idx in range(len(nums)):
            pairs=self.twoSum(nums[idx+1:],-nums[idx])
            if len(pairs)==0:
                continue
            for pair in pairs:
                new=[nums[idx]]+pair
                if tuple(new) not in d:
                    l.append(new)
                    d.add(tuple(new))
        return l

        