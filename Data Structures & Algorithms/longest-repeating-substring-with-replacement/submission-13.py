class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start=0
        d={}
        maxletter=0
        maxi=0
        end=0
        boucle=True
        while True:
            if s[end] not in d:
                d[s[end]]=1
            else:
                d[s[end]]+=1

            if d[s[end]]>=maxletter:
                maxletter=d[s[end]]


            condition = maxletter+k>=end-start+1
            if condition:
                if maxletter+k>=maxi : maxi=end-start+1
                if end == len(s)-1: return maxi
                end+=1
            else:
                d[s[start]]-=1
                start+=1
                if end == len(s)-1: return maxi
                end+=1

            if start==len(s)-1:
                return maxi




            
            
            
            

        