class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        
        def traverse(start, currentSum, temp):
            
            if currentSum==target:
                result.append(temp)
                return
            
            for i in range(start,len(candidates)):
                if (currentSum+candidates[i])>target:
                    return
                elif i>start and candidates[i]==candidates[i-1]:
                    continue
                else:
                    traverse(i+1,currentSum+candidates[i],temp+[candidates[i]])

        traverse(0,0,[]) 
        return result
