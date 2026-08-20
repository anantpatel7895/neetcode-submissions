class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in s:

            n = i

            if n in "({[":

                stack.append(n)
                continue

            else:

                if not stack:
                    print(stack)
                    return False

                top = stack.pop()
                print(stack)

                if ((n == ')' and top != '(') or
                    (n == '}' and top != '{') or
                    (n == ']' and top != '[')):
                    return False

        
        if stack:
            return False

        return True
        