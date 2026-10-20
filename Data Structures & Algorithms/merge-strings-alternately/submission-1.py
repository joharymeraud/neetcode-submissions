class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=""
        n=min(len(word1),len(word2))
        for i in range(n):
            word+=word1[i]
            word+=word2[i]
        return word + word1[n:]+word2[n:]
        