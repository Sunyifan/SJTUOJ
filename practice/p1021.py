import sys


n = int(sys.stdin.readline().rstrip())


def init_arr(n):
    arr = []
    for i in range(n):
        arr.append([])

        for j in range(n):
            arr[-1].append(None)

    return arr


class Direction:
    LEFT = 'left'
    RIGHT = 'right'
    DOWN = 'down'
    UP = 'up'


cur_x = cur_y = 0
cur_dir = Direction.RIGHT
arr = init_arr(n)


for i in range(n * n):
    arr[cur_x][cur_y] = i + 1

    if cur_dir == Direction.RIGHT:
        if cur_y == n - 1 or arr[cur_x][cur_y + 1] is not None:
            cur_dir = Direction.DOWN
            cur_x += 1
        else:
            cur_y += 1
    elif cur_dir == Direction.DOWN:
        if cur_x == n - 1 or arr[cur_x + 1][cur_y] is not None:
            cur_dir = Direction.LEFT
            cur_y -= 1
        else:
            cur_x += 1
    elif cur_dir == Direction.LEFT:
        if cur_y == 0 or arr[cur_x][cur_y - 1] is not None:
            cur_dir = Direction.UP
            cur_x -= 1
        else:
            cur_y -= 1
    elif cur_dir == Direction.UP:
        if cur_x == 0 or arr[cur_x - 1][cur_y] is not None:
            cur_dir = Direction.RIGHT
            cur_y += 1
        else:
            cur_x -= 1

for item in arr:
    print('      '.join([str(x) for x in item]))