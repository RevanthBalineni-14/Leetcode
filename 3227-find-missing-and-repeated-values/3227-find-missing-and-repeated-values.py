class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nset = set()
        n = len(grid)
        duplicate = -1
        for row in grid:
            for val in row:
                if val not in nset:
                    nset.add(val)
                else:
                    duplicate = val
        missing = ((n**2)*(n**2+1))//2 - sum(nset)
        return [duplicate, missing]