class Solution:
    def key(self,l1):
        l = [0]*26
        for i in range(len(l1)):
            l[ord(l1[i])-ord('a')]+=1
        return tuple(l) 

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for word in strs:
            if self.key(word) not in d:
                d[self.key(word)]=[word]
            else:
                d[self.key(word)].append(word)
        return list(d.values())       

        