class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        minimum = min(nums)
        maximum = max(nums)
        for num in nums:
            if num != minimum and num != maximum:
                return num 
