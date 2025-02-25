class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        bask = collections.defaultdict(int)
        l, total, res = 0, 0, 0
        for r in range(len(fruits)):
            bask[fruits[r]] += 1
            total += 1

            while len(bask) > 2:
                f = fruits[l]
                bask[f] -= 1
                total -= 1
                l += 1
                if not bask[f]:
                    bask.pop(f)
            res = max(total, res)
        return res