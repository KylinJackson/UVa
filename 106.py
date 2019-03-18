import math
import sys

'''
x = a^2-b^2
y = 2ab
z = a^2 + b^2
a,b互素 a>b
'''


# f = open('out.txt', 'w')


def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


for N in sys.stdin:
    log = dict()
    N = int(N)
    L = int(math.sqrt(N))
    ans1 = 0
    for i in range(1, L + 1):
        for j in range(i + 1, L + 1, 2):
            z = i ** 2 + j ** 2
            if z <= N and gcd(i, j) == 1:
                ans1 += 1
                x = j ** 2 - i ** 2
                y = 2 * i * j
                k = 1
                while k * z <= N:
                    log[x * k] = True
                    log[y * k] = True
                    log[z * k] = True
                    k += 1
    print(ans1, N - len(log))
    # print(ans1, N - len(log), file=f)
# f.close()
