class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        double = []
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        for key, value in count_dict.items():
            if value > 1:
                double.append(key)
        return double