class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        num = []

        while x != 0:
            num.append(x % 10)
            x //= 10

        if not num: 
            return 0

        reversed_num = int("".join(map(str, num))) * sign


        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0

        return reversed_num
