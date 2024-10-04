class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        n = len(skill)
        
        if (total%(n//2)) != 0:
            return -1
        target = total // (n // 2)
        
        skill_count = Counter(skill)
    
        chemistry_sum = 0 
        for s in skill:
            if skill_count[s] == 0:
                continue 

            complement = target - s  

            if skill_count[complement] > 0:
                chemistry_sum += s * complement
                skill_count[s] -= 1
                skill_count[complement] -= 1
            else:
                return -1

        return chemistry_sum