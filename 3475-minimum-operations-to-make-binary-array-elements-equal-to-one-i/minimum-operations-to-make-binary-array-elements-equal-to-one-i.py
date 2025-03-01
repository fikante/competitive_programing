from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l, res = 0, 0
        for r in range(2,len(nums)):
            if nums[l] == 0:
                for m in range(l,r+1):
                    if nums[m] == 0:
                        nums[m] = 1
                    else:
                        nums[m] = 0
                res += 1
            l += 1
        h = Counter(nums)
        if h[0] != 0:
            return -1
        return res