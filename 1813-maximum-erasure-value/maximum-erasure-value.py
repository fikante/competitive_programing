class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = 0
        current_sum = 0
        max_sum = 0
        window = set()
        for end in range(len(nums)):
            if nums[end] not in window:
                window.add(nums[end])
                current_sum += nums[end]
                max_sum = max(max_sum,current_sum)
            else:
                while nums[end] in window: 
                    window.remove(nums[start])
                    current_sum -= nums[start]
                    start += 1
                window.add(nums[end])
                current_sum += nums[end]
                max_sum = max(max_sum,current_sum)
        return max_sum