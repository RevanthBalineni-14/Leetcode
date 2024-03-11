class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        l = []
        for i in order:
                l.append(i*s.count(i))
        for i in s:
            if i not in order:
                l.append(i)
        return ''.join(l)