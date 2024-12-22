from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1m = Counter(s1)
        wm = Counter()
        s = 0
        for e in range(len(s2)):
            wm[s2[e]] += 1
            if e-s+1 > len(s1):
                wm[s2[s]] -= 1
                if wm[s2[s]] == 0:
                    del wm[s2[s]]
                s += 1
            if s1m == wm:
                return True
        return False