import sys
import os

# f = open('test.txt', 'r')
# f = open('out.txt', 'w')
'''
while True:
    n_str = f.readline()
    if n_str == '':
        break
    n = int(n_str)
    trans_list = []
    for m in range(n):
        trans_list.append(list(map(float, f.readline().split())))
        trans_list[m].insert(m, 1.)
'''
for line in sys.stdin:
    d = dict()
    path = dict()
    lane = list()
    trans_list = []
    n = int(line)
    for m in range(n):
        trans_list.append(list(map(float, input().split())))
        trans_list[m].insert(m, 1.)

    for start, end_list in enumerate(trans_list, start=1):
        for end, end_value in enumerate(end_list, start=1):
            d[(start, end, 1)] = end_value


    def floyd():
        for step in range(2, n + 1):
            for k in range(1, n + 1):
                for i in range(1, n + 1):
                    for j in range(1, n + 1):
                        if (i, j, step) not in d:
                            d[(i, j, step)] = 0
                        if d[(i, j, step)] < d[(i, k, step - 1)] * d[(k, j, 1)]:
                            d[(i, j, step)] = d[(i, k, step - 1)] * d[(k, j, 1)]
                            path[(i, j, step)] = k
                        if d[(i, j, step)] > 1.01 and i == j:
                            lane.insert(0, i)
                            while step > 1:
                                lane.insert(0, path[(i, j, step)])
                                j = path[(i, j, step)]
                                step -= 1
                            lane.insert(0, i)
                            return True
        return False


    if floyd():
        # f.write(' '.join(map(str, lane)))
        # f.write('\n')
        print(' '.join(map(str, lane)))
    else:
        # f.write('no arbitrage sequence exists')
        # f.write('\n')
        print("no arbitrage sequence exists")
# f.close()
