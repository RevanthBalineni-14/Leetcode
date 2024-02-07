class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        myl = [0]*62  
        mylist = []
        for i in s:
            if i.isdigit():
                myl[ord(i) - 48 + 52] += 1 
            else:
                myl[ord(i) - (97 if ord(i) > 96 else 39)] += 1
        for i in range(62):
            mylist.append((myl[i], i))
        
        mylist.sort(key=lambda x: x[0], reverse=True)
        res = []
        for i in range(len(mylist)):
            if mylist[i][1] >= 52:  
                mychar = chr(mylist[i][1] - 4)
            else:
                mychar = chr(mylist[i][1] + (39 if mylist[i][1] > 25 else 97))
            for j in range(mylist[i][0]):
                res.append(mychar)
                
        return "".join(res)
