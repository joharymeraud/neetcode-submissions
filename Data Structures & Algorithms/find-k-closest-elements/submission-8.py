class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        d=0
        fileparcours=deque()
        filemin=deque()
        mini=100000
        for i in range(len(arr)):
            num=arr[i]
            if i<=k-1:
                fileparcours.append(num)
                d+=abs(num-x)
            else:
                if d<mini:
                    mini=d
                    filemin=fileparcours.copy()

                last=fileparcours.popleft()
                d-=abs(last-x)

                fileparcours.append(num)
                d+=abs(num-x)
        if d<mini:
            mini=d
            filemin=fileparcours.copy()

        return list(filemin)              



        