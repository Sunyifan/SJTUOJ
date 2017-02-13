'''
1 2
3 4
'''

import sys


while True:
    line = [int(item) for item in sys.stdin.readline().rstrip().split()]

    if not line:
        break

    print(sum(line))
