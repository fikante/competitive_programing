class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = [str(digit) for digit in digits]
        digit = ''.join(str_digits)
        num = int(digit) + 1
        list_int = [int(n) for n in str(num)]
        return list_int
