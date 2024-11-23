class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = defaultdict(int)
        
        for row in matrix:
            pattern = ""
            for i in range(len(row)):
                pattern += str(row[i] if row[0] == 0 else (1 - row[i]))
            counter[pattern] += 1
            
        return max(counter.values())        