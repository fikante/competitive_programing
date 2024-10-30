class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hm = {}
        sum = 0
        for num in nums:
            hm[num] = hm.get(num, 0)+1
        
        for key, value in hm.items():
            if value == 1:
                sum += key
            else:
                continue
        return sum