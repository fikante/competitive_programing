class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        max_sum=[]
        for i in range(1,len(nums)):
            max_sum.append(nums[i]-nums[i-1])
        return max(max_sum)