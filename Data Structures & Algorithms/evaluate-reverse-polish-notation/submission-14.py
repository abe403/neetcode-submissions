class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        symbols = ("+", "-", "*", "/")

        res = 0

        second = 0
        first = 0

        for i in range(0, len(tokens), 1):
            cur = tokens[i]
            if cur in symbols:
                second = stack.pop()
                first = stack.pop()
                if cur == "+":
                    res = int(first + second)
                elif cur == "-":
                    res = int(first - second)
                elif cur == "*":
                    res = int(first * second)
                elif cur == "/":
                    res = int(first / second)
                stack.append(res)
            else:
                stack.append(int(cur))
        return stack[0]
