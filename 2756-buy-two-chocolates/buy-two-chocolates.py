class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        i = 0
        if (prices[i] + prices[i+1]) <= money:
            return money - (prices[i] + prices[i+1])
        else:
            return money
