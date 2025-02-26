class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        ans = 0
        left, middle = 0, 0
        for right in range(len(nums)):
            if nums[right] % 2:
                count += 1
            while count > k:
                if nums[left] % 2:
                    count -= 1
                left += 1
                middle = left
            if count == k:
                while not nums[middle] % 2:
                    middle += 1
                ans += (middle - left + 1)
        return ans