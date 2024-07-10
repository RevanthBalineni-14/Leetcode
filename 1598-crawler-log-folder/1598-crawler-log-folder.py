class Solution:
    def minOperations(self, logs: List[str]) -> int:
        mylist = []
        for i in logs:
            if i == "./":
                continue
            elif i=="../":
                if len(mylist)==0:
                    continue
                else:
                    mylist.pop(-1)
            else:
                    mylist.append(i)
                    
        return len(mylist)