class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        a = []
        for num in arr:
            count[num] = count.get(num, 0)+1
        for key,value in count.items():
            if key == value:
                a.append(key)
        if a:
            return max(a)
        return -1