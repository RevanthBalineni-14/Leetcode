class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        arr = []
        res = set()
        for i in tiles:
            arr.append(i)
        def traverse(cind, carr, cval):
            if cind == len(tiles):
                res.add(cval)
                return
            for index, i in enumerate(carr):
                traverse(cind+1, carr[:index]+carr[index+1:], cval + carr[index])
                traverse(cind+1, carr[:index]+carr[index+1:], cval)
        traverse(0, arr, "")
        res.remove("")
        return len(res)