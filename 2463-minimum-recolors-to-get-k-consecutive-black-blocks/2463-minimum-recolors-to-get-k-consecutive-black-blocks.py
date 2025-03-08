class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cb, cw = 0, 0
        for i in range(k):
            if blocks[i]=="B":
                cb += 1
            else:
                cw += 1
        
        res = cw
        for i in range(k, len(blocks)):
            if blocks[i]=="B":
                cb += 1
            else:
                cw += 1
            if blocks[i-k]=="B":
                cb -= 1
            else:
                cw -= 1
            res = min(res, cw)
        return res