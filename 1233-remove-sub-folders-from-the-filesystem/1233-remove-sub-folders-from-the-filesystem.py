class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        
        for i in folder:
            if not res:
                res.append(i)
            elif not i.startswith(res[-1]+'/'):
                res.append(i)
        
        return res