class Solution:
    def ispal(self,s):
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            else:
                i+=1
                j-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        skiped=False
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                if not skiped:
                    skiped=True
                    return (self.ispal(s[i+1:j+1]) or self.ispal(s[i:j]))
                else:
                    return False
            else:
                i+=1
                j-=1
        return True

             

        
        