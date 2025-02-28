from collections import Counter
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        window = {}
        total_unique = len(Counter(nums))
        left, count, res = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] not in window:
                count += 1
            window[nums[right]] = window.get(nums[right], 0) + 1

            while count == total_unique:
                res += len(nums) - right 
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    window.pop(nums[left])
                    count -= 1
                left += 1

        return res