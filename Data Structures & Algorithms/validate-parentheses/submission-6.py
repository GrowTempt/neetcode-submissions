class Solution:
    def isValid(self, s: str) -> bool:
        # Go through every char in S
        # Append all the opening characters to the stack
        # Check if the closing character and the top character is the same type, pop
        # If not, return false
        # If stack is not empty, return false, else return true
        stack = []
        for char in s:
            if char in ["{", "(", "["]:
                stack.append(char)
                continue

            if len(stack) != 0:
                top = stack[-1]
                if char == "}" and top == "{":
                    stack.pop()
                elif char == "]" and top == "[":
                    stack.pop()
                elif char == ")" and top == "(":
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
