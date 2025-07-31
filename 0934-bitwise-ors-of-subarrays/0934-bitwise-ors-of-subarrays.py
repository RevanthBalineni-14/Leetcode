class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        my_set = set(arr)
        curr = 0
        prev = set()
        prev.add(arr[0])
        for num in arr[1:]:
            temp = set()
            for p in prev:
                temp.add(num | p)
                my_set.add(num | p)
            prev = temp
            prev.add(num)

        return len(my_set)