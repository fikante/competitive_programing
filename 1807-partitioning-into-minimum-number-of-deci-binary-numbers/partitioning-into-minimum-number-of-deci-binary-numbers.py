class Solution:
    def minPartitions(self, n: str) -> int:
        digit = 0
        for i in range(len(n)):
            digit = max(digit, int(n[i]))
        return digit