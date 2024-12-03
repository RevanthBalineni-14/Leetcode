class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        arr = []
        arr.append(s[:spaces[0]])
        for i in range(1, len(spaces)):
            arr.append(s[spaces[i-1]:spaces[i]])
        arr.append(s[spaces[-1]:])
        return ' '.join(arr)