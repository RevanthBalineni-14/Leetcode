class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        s_positions = [(c, i) for i, c in enumerate(start) if c in 'LR']
        t_positions = [(c, i) for i, c in enumerate(target) if c in 'LR']
        
        # Check if the order and count of L and R are the same
        if len(s_positions) != len(t_positions):
            return False
        for (sc, si), (tc, ti) in zip(s_positions, t_positions):
            if sc != tc:  
                return False
            if sc == 'L' and si < ti: 
                return False
            if sc == 'R' and si > ti:
                return False
        
        return True