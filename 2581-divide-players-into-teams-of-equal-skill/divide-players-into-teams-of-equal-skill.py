class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        product = 0
        left = 0
        right = len(skill)-1
        skill.sort()
        sum = skill[left] + skill[right]
        while right > left:
            s = skill[left] + skill[right]
            if s == sum:
                product += skill[left]*skill[right]
                left += 1
                right -= 1
            else:
                return -1
        return product
