class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = 0
        ans = []
        for num in nums:
            if num < pivot: 
                ans.insert(less, num)
                less += 1
            elif num == pivot:
                ans.insert(less, num)
            else:
                ans.append(num)
        return ans