class Solution:
    def reverseWords(self, s: str) -> str:
        if s=="":
            return ""
        arr = s.split(" ")
        new = arr[0][::-1]
        for i in range(1,len(arr)):
            new += " "+arr[i][::-1]

        return new