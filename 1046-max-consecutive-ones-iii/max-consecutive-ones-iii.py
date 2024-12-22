class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        s = 0
        ml = 0
        c = 0
        for e in range(len(nums)):
            if nums[e] == 0:
                c += 1
            while c > k:
                if nums[s] == 0:
                    c -= 1
                s += 1
            ml = max(ml,e-s+1)
        return ml