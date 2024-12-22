from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pm=Counter(p)
        wm=Counter()
        result = []
        st=0
        for e in range(len(s)):
            wm[s[e]] += 1
            if e-st+1 > len(p):
                wm[s[st]] -= 1
                if wm[s[st]] == 0:
                    del wm[s[st]]
                st += 1
            if wm == pm:
                result.append(st)
        return result