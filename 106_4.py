import sys


# x = a^2-b^2
# y = 2ab
# z = a^2+b^2
# a,b互素, a>b

# f_out = open('out.txt', 'w')


def gcd(x, y):
    # 判断两个数是不是互质, x>y
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


prime_list = list()

L = 1000
N = 1000000
for i in range(1, L + 1):
    for j in range(i + 1, L + 1, 2):
        z = i ** 2 + j ** 2
        if z <= N and gcd(i, j) == 1:
            x = j ** 2 - i ** 2
            y = 2 * i * j

            if x > y:
                x, y = y, x
            prime_list.append((z, y, x))

prime_list.sort()

for n in sys.stdin:
    log = dict()
    n = int(n)
    prime_index = 0
    while True:
        if prime_index >= len(prime_list):
            break
        prime = prime_list[prime_index]
        if prime[0] <= n:
            prime_index += 1
            k = 1
            while k * prime[0] <= n:
                log[k * prime[0]] = True
                log[k * prime[1]] = True
                log[k * prime[2]] = True
                k += 1
        else:
            prime = prime_list[prime_index - 1]
            break
    # print(prime_index, n - len(log), file=f_out)
    print(prime_index, n - len(log))

# f_out.close()
