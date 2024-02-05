"""
Algorithm:

Declare a character stack S.
Now traverse the expression string exp.
1. If the current character is a starting bracket (‘(‘ or ‘{‘ or ‘[‘) then push it to stack.
2. If the current character is a closing bracket (‘)’ or ‘}’ or ‘]’) then pop from stack and if the popped character is the matching starting bracket then fine else parenthesis are not balanced.
After complete traversal, if there is some starting bracket left in stack then "not balanced"

# Time Complexity: O(n)
# Auxiliary Space: O(n) for stack.
"""


def is_balanced_paranthesis(expr):
    stack = []

    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:

            # Push the element in the stack
            stack.append(char)
        else:

            # If current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True


if __name__ == "__main__":
    expr = "{()}[]"
    if is_balanced_paranthesis(expr):
        print("Balanced")
    else:
        print("Not Balanced")
