class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        h = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(nums)):
            h[nums[r]] = h.get(nums[r], 0) + 1
            while h[0] == 2:
                h[nums[l]] -= 1
                l += 1
            res = max(h[1],res)
        if h[0] == 0:
            res -= 1
        return res