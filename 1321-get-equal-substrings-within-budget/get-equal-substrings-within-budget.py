class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        hashCost = {}
        left, cost, res = 0, 0, 0
        for right in range(len(s)):
            hashCost[right] = abs(ord(s[right]) - ord(t[right]))
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > maxCost:
                cost -= hashCost[left]
                hashCost.pop(left)
                left += 1
            res = max(res, right - left + 1)
        return res