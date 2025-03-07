class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right+1)
        sieve[0], sieve[1] = False, False
        for i in range(2, int(right**0.5)+1):
            if sieve[i]:
                for j in range(i*i, right+1, i):
                    sieve[j] = False
        prime_nums = [ind for ind in range(left, right+1) if sieve[ind]]
        if len(prime_nums)<2:
            return [-1, -1]

        cdist = 10**6
        res = [-1, -1]
        for i in range(len(prime_nums)-1):
            if (prime_nums[i+1]-prime_nums[i])<cdist:
                res = [prime_nums[i], prime_nums[i+1]]
                cdist = prime_nums[i+1]-prime_nums[i]
        return res