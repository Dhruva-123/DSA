##### Valid paranthesis is a common stack question.

class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {"}" : "{", "]":"[", ")":"("}
        pointer = 0
        if len(s) % 2 != 0:
            return False
        for item in s:
            pointer += 1
            if item in mapping.values():
                stack.append(item)
            else:
                if stack:
                    temp = stack.pop()
                    if temp != mapping[item]:
                        return False
                else:
                    return False
        if not stack and pointer == len(s):
            return True
        else:
            return False

        