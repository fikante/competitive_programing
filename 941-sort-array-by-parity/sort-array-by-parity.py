class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr=[]
        odd=[]
        if nums==[0]:
            return [0]
        for num in nums:
            if num%2==0:
                arr.append(num)
            else:
                odd.append(num)
        arr.extend(odd)
        return arr