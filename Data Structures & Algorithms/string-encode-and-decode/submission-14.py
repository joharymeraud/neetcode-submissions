class Solution:

    def encode(self, strs: List[str]) -> str:
        l=[]
        for string in strs:
            l.append(str(len(string)))
            l.append('w')
            l.append(string)
        return ''.join(l)


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        else:
            l=[]
            mot=""
            bkval = 0
            for i in range(len(s)):
                if s[i]=='w':
                    bkval = i
                    break
            cb = int(s[:bkval])

            for i in range(bkval+1,bkval+cb+1):
                mot+=s[i]
            l.append(mot)
            c=self.decode(s[bkval+cb+1:])
            return l+c






