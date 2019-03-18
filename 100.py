import sys

rs = {1: 1}


def get_res(n):
    if n in rs:
        return rs[n]
    elif n % 2 == 0:
        rs[n] = get_res(int(n / 2)) + 1
        return rs[n]
    else:
        rs[n] = get_res(int(3 * n + 1)) + 1
        return rs[n]


for line in sys.stdin:
    (i, j) = (int(x) for x in line.split())
    flag = False
    if i > j:
        i, j = j, i
        flag = True
    max_num = 0
    for k in range(i, j + 1):
        num = get_res(k)
        if num > max_num:
            max_num = num
    if flag:
        i, j = j, i
    print(i, j, max_num)
