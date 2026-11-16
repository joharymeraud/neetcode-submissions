class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=[0]*26
        current=[0]*26
        n1=len(s1)
        for c in s1:
            l[ord(c)-ord('a')]+=1
        for i,letter in enumerate(s2):
            if i <=n1-2:
                current[ord(letter)-ord('a')]+=1
            else:
                current[ord(letter)-ord('a')]+=1
                if current==l: return True
                current[ord(s2[i-n1+1])-ord('a')]-=1
        return False





        