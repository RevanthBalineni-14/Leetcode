class Solution:
    def smallestNumber(self, pattern: str) -> str:
        carr = []
        for i in range(1, len(pattern)+2):
            carr.append(i)

        res = float('inf')
        def traverse(curr, carr):
            nonlocal res

            if len(curr)==(len(pattern)+1):
                cpattern = ""
                for index in range(1, len(curr)):
                    if int(curr[index-1])<int(curr[index]):
                        cpattern += "I"
                    else:
                        cpattern += "D"
                if cpattern == pattern:
                    res = min(res, int(curr))
                    return True
                else:
                    return False
            
            for index, i in enumerate(carr):
                if traverse(curr + str(i), carr[:index]+carr[index+1:]):
                    return True

        traverse("", carr)
        return str(res)        