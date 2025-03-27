class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        count = 0
        ans = []
        for num in range(left, right + 1):
            for i in str(num):
                if int(i) == 0:
                    break
                elif num % int(i) == 0:
                    count += 1
            if count == len(str(num)):
                ans.append(num)
            count = 0
        return ans