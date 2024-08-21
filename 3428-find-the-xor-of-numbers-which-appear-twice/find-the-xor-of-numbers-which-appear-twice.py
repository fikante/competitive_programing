class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
    
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        result = 0
        for num, count in frequency.items():
            if count == 2:
                result ^= num
        
        return result

