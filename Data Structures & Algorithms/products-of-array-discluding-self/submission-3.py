class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        multg=[nums[0]] + [0]*(len(nums)-1)
        multd=[0]*(len(nums)-1)+[nums[len(nums)-1]]

        for i in range(1,len(nums)):
            multg[i] = multg[i-1]*nums[i]
            multd[len(nums)-1-i]=multd[len(nums)-i]*nums[len(nums)-1-i]

        output=[0]*len(nums)

        for i in range(len(nums)):
            if i ==0:
                output[i] = multd[i+1]
            elif i == len(nums)-1:
                output[i] = multg[i-1]
            else:
                output[i]=multg[i-1]*multd[i+1]
        return output
            
            
        