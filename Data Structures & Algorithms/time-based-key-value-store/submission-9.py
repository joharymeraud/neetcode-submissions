class TimeMap:

    def __init__(self):
        self.d={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key]=[(value,timestamp)]
        else:self.d[key].append((value,timestamp))

        

    def get(self, key: str, timestamp: int) -> str:
        val=self.d.get(key, [])
        if not val:
            return ""
        lo=0
        hi=len(val)-1
        while lo<hi:
            g=(hi+lo)//2+1
            condition = (val[g][1]<=timestamp)
            if condition: lo=g
            else:hi=g-1
        if (val[lo][1]<=timestamp):return val[lo][0]
        return ""

        
