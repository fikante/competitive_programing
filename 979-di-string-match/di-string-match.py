class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lo, hi = 0, len(s)
        perm = []
        
        for char in s:
            if char == 'I':
                perm.append(lo)
                lo += 1
            else:
                perm.append(hi)
                hi -= 1
        
        perm.append(lo)  # or hi, since lo == hi here
        return perm
