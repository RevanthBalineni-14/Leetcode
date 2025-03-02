class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mergedArray = []
        ln1, ln2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < ln1 and j < ln2:
            if nums1[i][0] == nums2[j][0]:
                mergedArray.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                mergedArray.append([nums1[i][0], nums1[i][1]])
                i += 1
            else:
                mergedArray.append([nums2[j][0], nums2[j][1]])
                j += 1
        if j < ln2:
            mergedArray.extend(nums2[j:])
        if i < ln1:
            mergedArray.extend(nums1[i:])
        return mergedArray