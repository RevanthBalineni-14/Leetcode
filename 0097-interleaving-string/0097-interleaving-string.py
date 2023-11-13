class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if (l1==0 and s2==s3) or (l2==0 and s1==s3):
            return True
        if (l1==0 and s2!=s3) or (l2==0 and s1!=s3):
            return False
        if (l1+l2)<l3 or (l1+l2)>l3:
            return False
        
        perm = [[False] * (l2+1) for _ in range (l1+1)]
        perm[0][0] = True

        for i in range(1, l1+1):
            perm[i][0] = perm[i-1][0] and s1[i-1]==s3[i-1]

        for j in range(1,l2+1):
            perm[0][j] = perm[0][j-1] and s2[j-1]==s3[j-1]
        
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                perm[i][j] = (perm[i-1][j] and s1[i-1]==s3[i+j-1]) or (perm[i][j-1] and s2[j-1]==s3[i+j-1])
        
        return perm[l1][l2]