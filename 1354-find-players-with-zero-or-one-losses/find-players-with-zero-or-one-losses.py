from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        all_win = set()
        lose1 = []

        winner = []
        loser = []
        for i in range(len(matches)):
            winner.append(matches[i][0])
            loser.append(matches[i][1])
        loser_dict = Counter(loser) 
        for num in winner:
            if num not in loser_dict:
                all_win.add(num)
        for key,value in loser_dict.items():
            if value == 1:
                lose1.append(key)
        all_win = sorted(all_win)
        lose1.sort()
        return [all_win,lose1]