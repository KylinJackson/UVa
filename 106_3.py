import sys

# x = a^2-b^2
# y = 2ab
# z = a^2+b^2
# a,b互素, a>b

f_out = open('out.txt', 'w')


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

# for prime in prime_list:
#     print(prime, file=f_out)

index = dict()


def find_index(number):
    min_distance = -1
    for ind in index:
        if number - ind > 0:
            if min_distance == -1 or min_distance > number - ind:
                min_distance = number - ind
    if min_distance == -1:
        return 0, 0
    return index[number - min_distance]


for n in sys.stdin:
    log = dict()
    n = int(n)
    prime_index, num = find_index(n)
    while True:
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
            index[prime[0]] = prime_index, len(log) + num
            break
    print(prime_index, n - len(log) - num, file=f_out)

f_out.close()
