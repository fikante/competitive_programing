class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return 
        average = (sum(nums[:k]))/k
        max_average = average
        for i in range(len(nums)-k):
            average = (average*k - nums[i] + nums[k+i])/k
            max_average = max(max_average, average)
        return max_average