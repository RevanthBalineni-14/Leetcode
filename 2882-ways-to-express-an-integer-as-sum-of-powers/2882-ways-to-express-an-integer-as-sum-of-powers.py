class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        self.memo = [[-1] * 301 for _ in range(301)]
        def recurrence(self, n, csum, x, num):
            if csum == n:
                return 1
            
            tmp = num**x

            if csum+tmp>n:
                return 0
            
            if self.memo[num][csum] != -1:
                return self.memo[num][csum]

            take = recurrence(self, n, csum+tmp, x, num+1)
            nottake = recurrence(self, n, csum, x, num+1)
            
            self.memo[num][csum] = (take+nottake)%mod
            return self.memo[num][csum]
        
        return recurrence(self, n, 0, x, 1)