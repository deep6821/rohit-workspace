"""
# https://www.geeksforgeeks.org/remove-brackets-algebraic-string-containing-operators/
Remove brackets from an algebraic string containing + and – operators

Simplify a given algebraic string of characters, ‘+’, ‘-‘ operators and parentheses. Output the simplified string
without parentheses.

Examples:
Input : "a-(b+c)"
Output : "a-b-c"

Input : "a-(b-c-(d+e))-f"
Output : "a-b+c+d+e-f"

The idea is to check operators just before starting of bracket, i.e., before character ‘(‘. If operator is -,
we need to toggle all operators inside the bracket. A stack is used which stores only two integers 0 and 1 to
indicate whether to toggle or not. We iterate for every character of input string. Initially push 0 to stack.
Whenever the character is an operator (‘+’ or ‘-‘), check top of stack. If top of stack is 0, append the same
operator in the resultant string. If top of stack is 1, append the other operator (if ‘+’ append ‘-‘) in the
resultant string.
"""


def simplify(input_str):
    length = len(input_str)

    # resultant String of max Length
    # equal to Length of input String
    res = [None] * length
    index = 0
    i = 0

    # create empty stack
    s = [0]

    while i < length:
        if input_str[i] == '+':

            # If top is 1, flip the operator
            if s[-1] == 1:
                res[index] = '-'
                index += 1

            # If top is 0, append the same operator
            if s[-1] == 0:
                res[index] = '+'
                index += 1

        elif input_str[i] == '-':
            if s[-1] == 1:
                res[index] = '+'
                index += 1

            elif s[-1] == 0:
                res[index] = '-'
                index += 1

        elif input_str[i] == '(' and i > 0:
            if input_str[i - 1] == '-':

                # x is opposite to the top of stack
                x = 0 if (s[-1] == 1) else 1
                s.append(x)

            # append value equal to top of the stack
            elif input_str[i - 1] == '+':
                s.append(s[-1])

        # If closing parentheses pop the stack once
        elif input_str[i] == ')':
            s.pop()

        # copy the character to the result
        else:
            res[index] = input_str[i]
            index += 1
        i += 1

    return res


# Driver Code
if __name__ == '__main__':

    # input_str = "a-(b+c)"
    # input_str = "a-(b-c-(d+e))-f"
    input_str = "a+(b-c)-(d-e)-(f+g)+(h+i)"
    result = simplify(input_str)
    print(">>>>>>>>>>>>>>\n", result)
    for expr in result:
        if expr is not None:
            print(expr, end=" ")
        else:
            break
    # print()
