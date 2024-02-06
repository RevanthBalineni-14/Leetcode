class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mydict = defaultdict(list)
        for i in strs:
            
            res = "".join(sorted(i))
            mydict[res].append(i)
            
        return list(mydict.values())