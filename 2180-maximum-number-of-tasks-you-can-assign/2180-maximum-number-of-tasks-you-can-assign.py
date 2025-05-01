class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        workers.sort()
        tasks.sort()

        def canAssign(mid):
            boosted = deque()
            w = len(workers)-1
            free_pills = pills

            for t in reversed(tasks[0:mid]):
                if boosted and boosted[0]>=t:
                    boosted.popleft()
                elif w>=0 and workers[w]>=t:
                    w -= 1
                else:
                    while w>=0 and (workers[w]+strength)>=t:
                        boosted.append(workers[w])
                        w-=1
                    if not boosted or free_pills == 0:
                        return False
                    free_pills -= 1
                    boosted.pop()
            return True
        
        low, high = 0, min(len(tasks), len(workers))
        while low < high:
            mid = (low + high + 1) // 2
            if canAssign(mid):
                low = mid
            else:
                high = mid - 1
        return low
