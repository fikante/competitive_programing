from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, findFirst):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    if findFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index
        
        first = binarySearch(nums, target, True)
        if first == -1:
            return [-1, -1]
        last = binarySearch(nums, target, False)
        return [first, last]
