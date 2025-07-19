class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for i in folder:
            if not res:
                res.append(i)
            else:
                if i.startswith(res[-1]+'/'):
                    continue
                else:
                    res.append(i)
        return res