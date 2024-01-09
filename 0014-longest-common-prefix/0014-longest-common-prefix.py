class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        com = ""
        start = strs[0]
        end = strs[-1]
        for i in range(min(len(start), len(end))):
            if start[i]!=end[i]:
                return com
            com += start[i]
        return com