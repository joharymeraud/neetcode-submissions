class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        left={"(","{","["}
        right={")","}","]"}
        corresp={"(":")","{":"}","[":"]"}

        pile=deque()
        for char in s:
            if char in left:
                pile.append(char)
            if char in right:
                if not pile:return False
                if corresp[pile.pop()]!=char:
                    return False
        if pile:return False
        return True
