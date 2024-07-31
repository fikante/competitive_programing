class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller_arr = []
        for i in range(len(nums)):
            count = 0
            j = 0
            while j < len(nums):
                if nums[i] > nums[j]:
                    count += 1
                j += 1
            smaller_arr.append(count)
        return smaller_arr