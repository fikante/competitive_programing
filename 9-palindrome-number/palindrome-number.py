class Solution:
    def isPalindrome(self, x: int) -> bool:
        # handle edge cases
        if x < 0:
            return False
        # containers
        reversed_num = 0
        original_x = x

        # reverse the number
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        return original_x == reversed_num