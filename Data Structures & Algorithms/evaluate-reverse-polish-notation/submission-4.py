class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        for ch in tokens:
            if ch in "-+*/":
                num1 = stack.pop()
                num2 = stack.pop()

                res = None
                if ch == "-":
                    res = int(num2) - int(num1)
                elif ch == "+":
                    res = int(num2) + int(num1)
                elif ch == "*":
                    res = int(num2) * int(num1)
                elif ch == "/":
                    res = int(int(num2) / int(num1))
                
                stack.append(res)
            else:
                stack.append(ch)

        return stack[0]
        