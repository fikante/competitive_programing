class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = set(["a","e","i","o","u"])
        cv = 0
        mv = 0
        st = 0
        for e in range(len(s)):
            if s[e] in v:
                cv += 1
            if e-st+1 == k:
                mv = max(cv,mv)
                if s[st] in v:
                    cv -= 1
                st += 1
        return mv