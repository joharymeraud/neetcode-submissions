class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        alphabet = set(string.ascii_letters)
        for i in range(10):
            alphabet.add(str(i))   
        i=0
        j=len(s)-1
        while i<=j:
            if s[i].lower() == s[j].lower():
                i+=1
                j-=1
                continue
            elif s[i] not in alphabet: 
                i+=1
                continue
            elif s[j] not in alphabet:
                j-=1
                continue
            elif s[i] !=s[j]:
                return False
        return True


        