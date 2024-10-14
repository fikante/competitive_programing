class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = ['']*len(score)
        hash_map = {score[i]: i for i in range(len(score))}
        score.sort(reverse = True)
        for j in range(len(score)):
            index = hash_map[score[j]]
            if j == 0:
                answer[index] = "Gold Medal"
            elif j == 1:
                answer[index] = "Silver Medal"
            elif j == 2:
                answer[index] = "Bronze Medal"
            else:
                answer[index] = f"{j+1}"
        return answer

