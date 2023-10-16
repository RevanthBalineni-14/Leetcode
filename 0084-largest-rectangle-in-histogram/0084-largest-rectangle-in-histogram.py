class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if heights is None:
            return 0
        maxr = 0
        st = []
        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1]>h:
                temp = st.pop()
                maxr=max(maxr, (i-temp[0])*temp[1])
                start = temp[0]
            st.append((start,h))
        for i,h in st:
            maxr=max(maxr, h*(len(heights)-i))
        return maxr