###### Pretty simple. It's just sliding window done correctly.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        right = 0
        left = 0
        seen = set()
        while right < len(s):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
                right += 1
                ans = max(right - left, ans)
        return ans

        