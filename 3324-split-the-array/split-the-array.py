class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        print(hm)
        for value in hm.values():
            if value >= 3:
                return False
        return True