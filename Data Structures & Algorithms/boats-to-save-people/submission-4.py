class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i=0
        j=len(people)-1
        k,actualbag=0,0
        while i<=j:
            actualbag+=people[j]
            j-=1
            if people[i]+actualbag<=limit:
                i+=1
            actualbag=0
            k+=1
        return k 
            


        