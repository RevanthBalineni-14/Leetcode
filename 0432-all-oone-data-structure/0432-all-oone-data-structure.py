class AllOne:

    def __init__(self):
        self.mydic = defaultdict(int)

    def inc(self, key: str) -> None:
        self.mydic[key] += 1

    def dec(self, key: str) -> None:
        self.mydic[key] -= 1
        if self.mydic[key]<1:
            self.mydic.pop(key)

    def getMaxKey(self) -> str:
        if not self.mydic:
            return ""
        cmax = max(self.mydic.values())
        for k in self.mydic.keys():
            if self.mydic[k] == cmax:
                return k

    def getMinKey(self) -> str:
        if not self.mydic:
            return ""
        cmin = min(self.mydic.values())
        for k in self.mydic.keys():
            if self.mydic[k] == cmin:
                return k


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()