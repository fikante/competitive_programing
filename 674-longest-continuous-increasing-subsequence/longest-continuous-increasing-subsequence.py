class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        s = 0
        ml = 0
        cl = 0
        if len(nums) == 1:
            return nums[s]
        for e in range(1,len(nums)):
            if nums[e] <= nums[e-1]:
                s = e
            cl = e-s+1
            ml = max(cl,ml)
        return ml