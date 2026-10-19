class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        P=[nums[0]]
        for i in range(1,len(nums)):
            P.append(nums[i]+P[i-1])
        d={}
        e=0
        for i in range(len(nums)):
            if i==0:
                d[nums[0]]=1
                if nums[0]==k:
                    e+=1
            else:
                if P[i]-k in d:
                    e+=d[P[i]-k]
                if P[i]==k:
                    e+=1
                if P[i] in d:
                    d[P[i]]+=1
                else:
                    d[P[i]]=1
        return e 


            

        




        