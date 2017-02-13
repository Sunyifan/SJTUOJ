'''
input:

4 5
1 2 3 4 5
6 7 8 0 0
0 9 2 2 3
3 0 0 0 1
3 3
'''

garden_length, garden_width = map(int, raw_input().split())
garden_production = []

for i in range(garden_length):
    garden_production.append(map(int, raw_input().split()))


try_length, try_width = map(int, raw_input().split())


sum_prod = []

for l in range(garden_length):
    this_prod = []

    for w in range(garden_width - try_width + 1):
        if w == 0:
            last_sum = sum(garden_production[l][w: w + try_width])
        else:
            last_sum = last_sum - garden_production[l][w - 1] + garden_production[l][w + try_width - 1]

        this_prod.append(last_sum)

    sum_prod.append(this_prod)


cur_sums = []
last_sums = []
max_sum = 0

for l in range(garden_length - try_length + 1):
    for w in range(len(sum_prod[l])):
        if l == 0:
            cur_sum = sum([_s[w] for _s in sum_prod[l: l + try_length]])
        else:
            cur_sum = last_sums[w] - sum_prod[l - 1][w] + sum_prod[l + try_length - 1][w]

        cur_sums.append(cur_sum)
        max_sum = max_sum if max_sum > cur_sum else cur_sum

    last_sums = cur_sums
    cur_sums = []

print(max_sum)