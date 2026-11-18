class Solution:
    def windowExpansion(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            odd = self.windowExpansion(s, i, i)
            even = self.windowExpansion(s, i, i + 1)
            if len(odd) > len(ans):
                ans = odd
            if len(even) > len(ans):
                ans = even
        return ans