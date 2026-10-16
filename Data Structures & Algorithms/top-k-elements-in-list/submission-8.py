class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[[] for i in range(10001)]
        r=[]
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        for num,frequence in d.items():
            l[frequence].append(num)
        for i in range(len(l)-1,-1,-1):
            if len(l[i]) !=0:
                r+=l[i]
            if len(r)==k:
                return r 
        




            