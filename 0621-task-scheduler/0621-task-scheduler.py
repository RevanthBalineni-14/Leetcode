class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mydic={}
        time = 0
        for i in tasks:
            if i in mydic:
                mydic[i]+=1
            else:
                mydic[i]=1
            
        maxheap = [-cnt for cnt in mydic.values()]
        heapq.heapify(maxheap)

        queue = deque()

        while queue or maxheap:
            time+=1

            if maxheap:
                crt = heapq.heappop(maxheap)
                crt+=1
                if crt!=0:
                    queue.append([time+n, crt])
            if queue and queue[0][0]==time:
                heapq.heappush(maxheap, queue.popleft()[1])
        
        return time