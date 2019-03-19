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
            if min_distance == -1 and min_distance > number - ind:
                min_distance = number - ind
    return number - min_distance


for n in sys.stdin:
    log = dict()
    n = int(n)

    prime_index = 0
    while True:
        if (prime_list[prime_index])[0] <= n:
            prime_index += 1
            k = 1
            while k * (prime_list[prime_index])[0] <= n:
                log[(prime_list[prime_index])[0] * k] = True
                log[(prime_list[prime_index])[1] * k] = True
                log[(prime_list[prime_index])[2] * k] = True
                k += 1
        else:
            index[prime_list[prime_index][0]] = prime_index
            break

    print(prime_index + 1, n - len(log), file=f_out)

f_out.close()
