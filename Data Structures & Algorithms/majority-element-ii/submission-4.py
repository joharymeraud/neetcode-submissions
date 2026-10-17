class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        l=[]
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        for nombre,freq in d.items():
            if freq > len(nums)//3:
                l.append(nombre)
        return l 

        