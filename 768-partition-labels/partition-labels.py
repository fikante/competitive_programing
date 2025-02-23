class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {char: i for i,char in enumerate(s)}
        size, end = 0, 0
        result = []

        for i, char in enumerate(s):
            size += 1
            end = max(end, lastIndex[char])

            if i == end:
                result.append(size)
                size = 0
        return result