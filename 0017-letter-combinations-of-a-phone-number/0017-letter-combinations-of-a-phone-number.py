class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits)==0):
            return []
        result = []
        temp = ""
        dictionary = {}
        dictionary['2'] = ['a','b','c']
        dictionary['3'] = ['d','e','f']
        dictionary['4'] = ['g','h','i']
        dictionary['5'] = ['j','k','l']
        dictionary['6'] = ['m','n','o']
        dictionary['7'] = ['p','q','r','s']
        dictionary['8'] = ['t','u','v']
        dictionary['9'] = ['w','x','y','z']
        def recurse(rdigits,temp):
            if len(temp) == len(digits):
                result.append(temp)
                return
            crt = dictionary[rdigits[0]]
            for i in crt:
                recurse(rdigits[1:],temp+i)
        
        recurse(digits, temp)
        return result
            