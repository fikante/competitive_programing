class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        divisor_map = {}
        good_pairs = 0
        for num in nums2:
            divisor = num * k
            if divisor in divisor_map:
                divisor_map[divisor] += 1
            else:
                divisor_map[divisor] = 1
        for num in nums1:
            for divisor in divisor_map:
                if num % divisor == 0:
                    good_pairs += divisor_map[divisor]
        
        return good_pairs
