class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)
        for num in nums:
            count[num] = count.get(num,0) + 1
        for key,value in count.items():
            if value > (n/2):
                return key
        return -1