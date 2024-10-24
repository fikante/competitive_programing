class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        another = []
        # hm = {}
        for num in arr2:
            for i in range(len(arr1)):
                if arr1[i] == num:
                    ans.append(arr1[i])
        for j in arr1:
            if j not in ans:
                another.append(j)
                another.sort()
        return ans + another