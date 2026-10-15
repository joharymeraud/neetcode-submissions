class Solution:
    @staticmethod
    def prefixe(w1,w2):
        prefix=""
        for i in range(min(len(w1),len(w2))):
            if w1[i]==w2[i]:
                prefix+=w1[i]
            else:
                return prefix
        return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1,len(strs)):
            prefix = self.prefixe(prefix,strs[i])
        return prefix
        


            

        