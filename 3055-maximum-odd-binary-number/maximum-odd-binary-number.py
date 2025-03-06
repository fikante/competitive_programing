class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        len_of_1 = s.count("1")
        n = len(s)
        return '1'*(len_of_1 - 1) + '0'*(n - len_of_1) + '1'