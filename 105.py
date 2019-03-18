import sys

height = dict()
max_right = 0
for line in sys.stdin:
    l, h, r = map(int, line.split())
    if r > max_right:
        max_right = r
    for x in range(l, r):
        if x not in height or height[x] < h:
            height[x] = h
for i in range(1, max_right):
    if i - 1 not in height and i in height:
        print('%d %d ' % (i, height[i]), end='')
    elif i - 1 in height and i not in height:
        print('%d %d ' % (i, 0), end='')
    elif i - 1 not in height and i not in height:
        continue
    elif height[i] != height[i - 1]:
        print('%d %d ' % (i, height[i]), end='')
print('%d 0' % max_right)
