class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        left = 0
        right = len(numbers)-1
        while right > left:
            if numbers[left] + numbers[right] == target:
                ans.append(left+1)
                ans.append(right+1)
                break
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return ans