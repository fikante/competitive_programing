class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        char_count = {}

        for char in stones:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        for jewel in jewels:
            if jewel in char_count:
                count += char_count[jewel]
        return count