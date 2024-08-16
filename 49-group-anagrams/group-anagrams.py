from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_anagram = defaultdict(list)
        grouped_anagram = []
        for s in strs:
            sorted_s = tuple(sorted(s))
            map_anagram[sorted_s].append(s)
        return [values for values in map_anagram.values()]