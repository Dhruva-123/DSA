from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        seen = defaultdict(int)

        while right < len(s):
            if seen[s[right]] == 1:
                while seen[s[right]] == 1:
                    seen[s[left]] -= 1
                    left += 1

            seen[s[right]] += 1
            ans = max(ans, right + 1 - left)

            right += 1

        return ans