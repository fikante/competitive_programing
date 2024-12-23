class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        cd = st = 0
        md = float('inf')
        e = k-1
        num = sorted(nums)
        if len(nums) == 1:
            return 0
        while e < len(num):
            md = min(md,num[e]-num[st])
            st += 1
            e += 1
        return md