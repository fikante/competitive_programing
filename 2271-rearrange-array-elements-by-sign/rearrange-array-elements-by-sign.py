class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = 0, 1
        n = len(nums)
        ans = [0] * n
        for num in nums:
            if num > 0:
                ans[positive] = num
                positive += 2
            else:
                ans[negative] = num
                negative += 2
        return ans