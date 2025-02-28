class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left, count = 0, 0
        total = sum(arr[:k])
        if (total) >= threshold*k:
            count += 1
        for right in range(k,len(arr)):
            total += arr[right]
            total -= arr[left]
            if (total) >= threshold*k:
                count += 1
            left += 1
        return count
