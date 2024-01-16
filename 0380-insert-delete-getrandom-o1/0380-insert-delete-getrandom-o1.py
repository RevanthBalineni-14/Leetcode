class RandomizedSet:

    def __init__(self):
        self.mylist = []
        self.mymap = {}

    def insert(self, val: int) -> bool:
        if val in self.mymap:
            return False
        
        self.mylist.append(val)
        self.mymap[val] = len(self.mylist)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mymap:
            return False
        idx = self.mymap[val]
        self.mylist[idx] = self.mylist[-1]
        self.mymap[self.mylist[-1]] = idx
        self.mylist.pop()
        del self.mymap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.mylist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()