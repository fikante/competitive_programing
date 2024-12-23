class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        alnum_s = ''.join(char for char in lower_s if char.isalnum())
        left = 0
        right = len(alnum_s) - 1
        while left < right:
            if alnum_s[left] != alnum_s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True