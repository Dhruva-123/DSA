# Apparently there are 2 different approaches here. One is ugly, but technically speaking, it has lower complexity. One is more beautiful.


## approach 1:
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict1 = defaultdict(list)

        for item in strs:
            count = [0] * 26

            for char in item:
                count[ord(char) - ord('a')] += 1

            dict1[tuple(count)].append(item)

        return list(dict1.values())
    
    
## approach 2:

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict1 = defaultdict(list)
        for item in strs:
            temp = tuple(sorted(item))
            dict1[temp].append(item)
        return list(dict1.values())