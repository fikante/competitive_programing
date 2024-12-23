class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        cd = 0
        md = float('inf')
        st = 0
        num = sorted(nums)
        if len(nums) == 1:
            return 0
        for e in range(len(num)):
            if e-st+1 == k:
                cd = max(num[st:e+1]) - min(num[st:e+1])
                md = min(md,cd)
                st += 1
        return md