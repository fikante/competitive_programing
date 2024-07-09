class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        tar_ind=[]
        for i in range(len(nums)):
            if nums[i]==target:
                tar_ind.append(i)
        return tar_ind