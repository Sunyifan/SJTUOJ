'''
4
(())
(()

)(
'''

import sys
N = int(sys.stdin.readline())


def is_legal_exp(bracket_text):
    if not len(bracket_text):
        return 'NO'

    stack = []

    for _char in bracket_text:
        if _char == '(':
            stack.append(_char)
        else:
            if len(stack):
                stack.pop()
            else:
                return 'NO'

    return 'YES' if not len(stack) else 'NO'

for i in range(N):
    bracket_text = sys.stdin.readline().rstrip()
    print(is_legal_exp(bracket_text))
