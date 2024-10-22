class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        hm = {}
        n = len(nums) - 1 
        for i in range(n):
            if nums[i] == key:
                if nums[i+1] in hm:
                    hm[nums[i+1]] += 1
                else:
                    hm[nums[i+1]] = 1
        if hm: 
            max_key = max(hm, key=hm.get)
            return max_key
        return -1 
