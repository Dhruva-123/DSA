class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        i = 0
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        ans = 0
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            ans = ans * 10 + digit
            i += 1
        ans *= sign
        return max(INT_MIN, min(ans, INT_MAX))