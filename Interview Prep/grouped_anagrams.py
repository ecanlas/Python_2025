from typing import List
from collections import defaultdict

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagram_map[key].append(word)

        return list(anagram_map.values())

# Example usage:
sol = Solution()
print(sol.group_anagrams(["eat","tea","tan","ate","nat","bat"]))