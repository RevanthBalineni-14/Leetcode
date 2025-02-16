class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        cset = []
        carr = []
        for i in range(n, 0, -1):
            cset.append(i)

        for i in range(1, 2*n):
            carr.append(0)
        
        def isValid(cind, carr, i):
            if cind<len(carr) and (cind+i)<len(carr) and carr[i+cind]==0:
                return True
            return False

        def traverse(cset, carr, cind):
            if cind<len(carr) and carr[cind]!=0:
                while cind<len(carr) and carr[cind]!=0:
                    cind += 1
            if cind == len(carr):
                return True
            for index, i in enumerate(cset):
                if i==1:
                    carr[cind] = 1
                    if traverse(cset[0:index]+cset[index+1:], carr, cind+1):
                        return True
                    carr[cind] = 0
                else:
                    if isValid(cind, carr, i):
                        carr[cind] = i
                        carr[cind+i] = i
                        if traverse(cset[0:index]+cset[index+1:], carr, cind+1):
                            return True
                        carr[cind] = 0
                        carr[cind+i] = 0
            return False
        traverse(cset, carr, 0)
        return carr