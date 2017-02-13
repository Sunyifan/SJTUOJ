'''
0 1 1 11

'''

a, b, c, N = map(int, raw_input().split())

month_cnt = [1, 0, 0]
new_cnt = [0, 0, 0]

for i in range(N):

    new_cnt[0] = month_cnt[0] * a + month_cnt[1] * b + month_cnt[2] * c
    new_cnt[1] = month_cnt[0]
    new_cnt[2] = month_cnt[1] + month_cnt[2]
    month_cnt = new_cnt
    new_cnt = [0, 0, 0]

print(sum(month_cnt))
