class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pile=deque()
        results=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while pile and temp > pile[-1][0]:
                info=pile.pop()
                results[info[1]]=i-info[1]
            pile.append((temp,i))
        return results




        