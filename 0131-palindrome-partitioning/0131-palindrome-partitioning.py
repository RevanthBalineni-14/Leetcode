class Solution:
    def partition(self, s: str) -> List[List[str]]:
        mydic = defaultdict(list)
        def ispallindrome(s):
            if s == s[::-1]:
                return True

        def traverse(index, mydic):
            if index in mydic:
                return mydic[index]
            if index == len(s):
                return [[]]
            end = index
            while end < (len(s)+1):
                if ispallindrome(s[index:end+1]):
                    for subpartition in traverse(end + 1, mydic):
                        mydic[index].append([s[index:end+1]] + subpartition)
                end += 1

            return mydic[index]
        
        traverse(0, mydic)
        return mydic[0]