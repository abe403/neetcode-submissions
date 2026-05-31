class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        symbols = ("+", "-", "*", "/")

        res = 0

        second = 0
        first = 0

        if len(tokens) == 1:
                if tokens[0] not in symbols: return int(tokens[0])
                else: return 0

        for i in range(0, len(tokens), 1):
            cur = tokens[i]
            if cur in symbols:
                second = stack.pop()
                first = stack.pop()
                match cur:
                    case "+":
                        res = first + second
                    case "-":
                        res = first - second
                    case "*":
                        res = first * second
                    case "/":
                        res = int(first / second)
                stack.append(res)
            else:
                stack.append(int(cur))
        return stack[0]
