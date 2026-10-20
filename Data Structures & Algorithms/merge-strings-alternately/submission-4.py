class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=[]
        n=min(len(word1),len(word2))
        for i in range(n):
            word.append(word1[i])
            word.append(word2[i])
        word.append(word1[n:])
        word.append(word2[n:])
        return "".join(word)