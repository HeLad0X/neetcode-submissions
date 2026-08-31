class Solution:
    def isValid(self, s: str) -> bool:
        bracket_match = {
            ")" : "(",
            '}' : '{',
            ']' : '['
        }

        bracket_stack = []
        for ch in s:
            if ch in "({[":
                bracket_stack.append(ch)
            elif ch in ")}]":
                if len(bracket_stack) == 0: return False
                if bracket_stack[-1] == bracket_match[ch]:
                    bracket_stack.pop()
                else:
                    return False
            else:
                continue

        return len(bracket_stack) == 0
        