class Solution:
    def balancedStringSplit(self, s: str) -> int:
        middle = 0
        count = 0
        for string in s:
            if string == "R":
                middle += 1
            elif string == "L":
                middle -= 1
            if middle == 0:
                count += 1
        return count