class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0
        right = -1
        for i,char in enumerate(word):
            if char == ch:
                right = i
                break
        if right == -1:
            return word
        l_word = list(word)
        while left < right:
            l_word[left], l_word[right] = l_word[right], l_word[left]
            right -= 1
            left += 1
        return ''.join(l_word)