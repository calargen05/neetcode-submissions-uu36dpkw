class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((value,timestamp))
        else:
            self.timemap[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        l,r = 0,len(self.timemap[key])-1
        found_val = ''
        while l <= r:
            mid = (l + r) // 2
            if self.timemap[key][mid][1] == timestamp:
                return self.timemap[key][mid][0]
            if self.timemap[key][mid][1] > timestamp:
                r = mid - 1
            else:
                found_val = self.timemap[key][mid][0]
                l = mid + 1
        return found_val
