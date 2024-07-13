from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        dirs = [i for i in directions]
        zarr = sorted(zip(positions, healths, dirs), key=lambda x: x[0])
        zarr = [list(t) for t in zarr]
        st = []
        res = {}
        for i in range(len(zarr)):
            if not st and zarr[i][2] == "L":
                res[zarr[i][0]] = zarr[i][1]
            elif st and zarr[i][2] == "L":
                while st and st[-1][1] < zarr[i][1]:
                    st.pop()
                    zarr[i][1] -= 1
                
                if not st:
                    res[zarr[i][0]] = zarr[i][1]
                elif st and st[-1][1] > zarr[i][1]:
                    st[-1][1] -= 1
                else:
                    st.pop()
            else:
                st.append([zarr[i][0], zarr[i][1]])
        
        for i in st:
            res[i[0]] = i[1]
        
        finalres = []
        for i in positions:
            if i in res.keys():
                finalres.append(res[i])
        
        return finalres
