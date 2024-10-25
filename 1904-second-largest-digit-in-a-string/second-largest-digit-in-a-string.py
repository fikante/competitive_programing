class Solution:
    def secondHighest(self, s: str) -> int:
        hm = {}
        arr = []
        for index, char in enumerate(s):
            if char.isdigit():
                hm[index] = char
        if hm:
            max_val = max(hm.values())
        else:
            return -1
        for value in hm.values():
            if value != max_val:
                arr.append(value)
        if arr:
            second_max = max(arr)
        else:
            return -1
        return int(second_max)