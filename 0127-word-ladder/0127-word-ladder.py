class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        
        nl = collections.defaultdict(list)
        wordList.append(beginWord)
        

        for word in wordList:
            for i in range(len(word)):
                patter = word[:i]+"&"+word[i+1:]
                nl[patter].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        cl=1
        while q:
            for i in range(len(q)):
                crt  = q.popleft()
                if crt == endWord:
                    return cl
                for j in range(len(crt)):
                    patter = crt[:j]+"&"+crt[j+1:]
                    for neighbor in nl[patter]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            cl+=1

        return 0