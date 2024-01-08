class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(0, len(nums) - 3):
            # Skip duplicate elements for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                # Skip duplicate elements for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                t = target - nums[i] - nums[j]
                k, l = j + 1, len(nums) - 1

                while k < l:
                    if nums[k] + nums[l] == t:
                        res.append([nums[i], nums[j], nums[k], nums[l]])

                        # Skip duplicate elements for k
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1

                        # Skip duplicate elements for l
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1

                        k += 1
                        l -= 1
                    elif nums[k] + nums[l] < t:
                        k += 1
                    else:
                        l -= 1

        return res
