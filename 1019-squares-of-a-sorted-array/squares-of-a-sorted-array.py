class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr=[]
        for num in nums:
            sqr.append(pow(num,2))
        sqr.sort()
        return sqr