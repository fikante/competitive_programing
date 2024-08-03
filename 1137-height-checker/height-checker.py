class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        h = 0
        e = 0
        count = 0
        while h < len(heights):
            if heights[h] != sorted_heights[e]:
                count += 1
            h += 1
            e += 1
        return count
