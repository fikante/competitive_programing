class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == 0:
                if nums[right] == 0:
                    right += 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right += 1
            elif nums[left] != 0:
                left += 1
                right += 1
        return nums
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # l, r = 0,0
        # while r < len(nums):
        #     if nums[r] != 0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        #     r += 1