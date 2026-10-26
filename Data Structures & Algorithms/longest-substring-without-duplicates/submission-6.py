class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":return 0
        d=set()
        i=0
        maxi = 0 
        for j in range(len(s)):
            if s[j] not in d:
                d.add(s[j])
            else:
                if j-i > maxi: maxi=j-i
                while s[j] in d:
                    d.remove(s[i])
                    i+=1
                d.add(s[j])
        if j-i+1>maxi:maxi=j-i+1
        return maxi
                
            
        