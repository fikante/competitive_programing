class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        c_l = 0
        c_s = 0
        min_l = float('inf')
        for e in range(len(nums)):
            c_s += nums[e]
            while c_s >= target:
                c_l = e-s+1
                min_l = min(c_l,min_l)
                c_s -= nums[s]
                s += 1
        if min_l == float('inf'):
            return 0
        return min_l