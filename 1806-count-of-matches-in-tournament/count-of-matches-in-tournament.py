class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n != 1:
            if n % 2 != 0:
                matches = (n-1)/2
                n = matches + 1
            else:
                matches = n/2
                n = matches
            count += int(matches)
        return count