class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        def search(arr, st, end, target):
            while st <= end:
                mid = (st + end)//2
                if arr[mid]==target:
                    return True
                elif arr[mid] < target:
                    st = mid + 1
                else:
                    end = mid - 1
            return False
        
        for i in range(len(arr)):
            if search(arr, i+1, len(arr)-1, 2*arr[i] if arr[i]>0 else (arr[i]//2 if arr[i]%2==0 else float('inf'))):
                return True
        
        return False