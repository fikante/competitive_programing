import math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        comb_map = Counter(nums)
        for value in comb_map.values():
            if value > 1:
                count += math.comb(value,2)
        return count